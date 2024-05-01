
import pandas as pd
import requests
import numpy as np

## 트래픽 기준 상위 1,000,000개 도메인 data 저장할 경로
data_file = 'nromal_data.csv'

## CSV 파일 읽기 (도메인, 순위, 날짜 정보 포함)
df = pd.read_csv('nromal_1M.csv')

## 이미 처리된 도메인 데이터 불러오기
processed_domains = set()
try:
    con_df = pd.read_csv(data_file)
    for index, row in con_df.iterrows():
        processed_domains.add(row[0])
except FileNotFoundError:
    pass

for index, row in df.iterrows():
    domain = row['domain_name']
    url = f'http://www.{domain}'  # URL 생성

    ## 이미 처리된 도메인인 경우 스킵
    if domain in processed_domains:
        print(f"Skipping domain {domain} (already processed)")
        continue

    try:
        ## request 요청
        response = requests.get(url, timeout=600)

        ## 저장할 data 정리
        result_row = {
            'Domain': domain,
            'URL': url,
            'HTML': response.content.decode(response.encoding),
            'Headers': dict(response.headers),
            'URL_Destination': response.url,
            'History': [h.url for h in response.history],
            'Encoding': response.encoding,
            'Elapsed_Time': response.elapsed.total_seconds(),
            'Request': {
                'Method': response.request.method if hasattr(response.request, 'method') else None,
                'URL': response.request.url if hasattr(response.request, 'url') else None,
                'Headers': dict(response.request.headers) if hasattr(response.request, 'headers') else None,
                'Body': response.request.body if hasattr(response.request, 'body') else None,
                'Params': response.request.params if hasattr(response.request, 'params') else None,
                'Cookies': dict(response.request._cookies) if hasattr(response.request, '_cookies') else None,
                'Auth': response.request.auth if hasattr(response.request, 'auth') else None
            }
        }

    ## 요청 거부, 시간 초과 등이 발생한 경우
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        ## 원인 파악을 위한 빈 도메인과 만든 url만 있는 data 형성
        result_row = {
            'Domain': domain,
            'URL': url,
            'HTML': '',
            'Headers': {},
            'URL_Destination': '',
            'History': [],
            'Encoding': '',
            'Elapsed_Time': 0,
            'Request': {
                'Method': None,
                'URL': None,
                'Headers': None,
                'Body': None,
                'Params': None,
                'Cookies': None,
                'Auth': None
            }
        }
    result_row = pd.DataFrame([result_row])
    result_row.to_csv(data_file, mode='a', header=False, index=False)
