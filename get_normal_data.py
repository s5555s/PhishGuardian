import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import os
import gzip
import gc
import time

# 로깅 설정
logging.basicConfig(filename='fetch_html.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# 주어진 도메인에 대한 HTML 콘텐츠를 가져오는 함수
def fetch_html(domain, rank, max_retries=3):
    url = f"http://{domain.strip('.')}"
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            logging.info(f"Successfully fetched {url}")
            return {'rank': rank, 'domain': domain, 'url': url, 'html': response.text}
        except requests.RequestException as e:
            attempts += 1
            logging.error(f"Failed to fetch {url}: {e}, attempt {attempts}")
            time.sleep(1)  # 재시도 전에 잠시 대기
        except Exception as e:
            logging.critical(f"Critical error fetching {url}: {e}")
            break
    return {'rank': rank, 'domain': domain, 'url': url, 'html': None}

# 도메인을 처리하고 HTML 콘텐츠를 가져오는 함수
def process_domains(df, max_workers=20):
    successful = []
    failed = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_html, row['domain_name'], row['output_rank']): row for _, row in df.iterrows()}
        for future in as_completed(futures):
            result = future.result()
            if result['html'] is not None:
                successful.append(result)
            else:
                failed.append(result)
    
    return successful, failed

# CSV 파일을 gzip으로 압축하여 저장하는 함수
def save_compressed_csv(data, filename):
    df = pd.DataFrame(data)
    with gzip.open(filename, 'wt', encoding='utf-8') as f:
        df.to_csv(f, index=False)

# CSV를 읽고, 도메인을 처리하고, 결과를 저장하는 메인 로직
def main():
    file_path = r"E:\캡스톤\top1M.csv"  # 경로를 원시 문자열로 처리
    df = pd.read_csv(file_path)
    
    # 출력 디렉토리가 존재하는지 확인
    os.makedirs('output', exist_ok=True)
    
    # 도메인을 10,000개씩 배치로 처리
    batch_size = 10000
    num_batches = (len(df) + batch_size - 1) // batch_size
    for i in range(num_batches):
        batch_df = df[i * batch_size:(i + 1) * batch_size]
        try:
            successful, failed = process_domains(batch_df)
        
            # 성공한 연결을 압축된 CSV에 저장
            if successful:
                save_compressed_csv(successful, f'output/successful_{i + 1}.csv.gz')
            
            # 실패한 연결을 압축된 CSV에 저장
            if failed:
                save_compressed_csv(failed, 'output/failed.csv.gz')
            
            # 가비지 컬렉션 호출하여 메모리 정리
            del successful
            del failed
            gc.collect()
        except Exception as e:
            logging.critical(f"Batch {i} processing failed: {e}")
            # 중간 저장된 데이터를 로그로 남기고 다음 배치로 넘어갑니다.
            continue

if __name__ == "__main__":
    main()
