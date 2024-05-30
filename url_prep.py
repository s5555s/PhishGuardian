import requests
import urllib.parse
import re
import statistics
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup


def read_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# Helper function to count words in a URL
def count_words(url):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path.split('/')
    words = [re.split(r'\W+', word) for word in path if word]
    words = [item for sublist in words for item in sublist]
    return words

# Helper function to get the text content of a web page
def get_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        return ""
    return ""

# Function to check if a word is a brand name
def is_brand_name(word):
    brand_names = read_file_to_list('allbrands.txt')
    return word.lower() in brand_names

def get_global_rank_from_meta(domain):
    url = f'https://hypestat.com/info/{domain}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve data for {domain}, status code: {response.status_code}"

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        meta_description = soup.find('meta', attrs={'name': 'description'})['content']
        rank_start = meta_description.find("ranked") + len("ranked ")  # 'ranked ' 이후 위치 찾기
        rank_end = meta_description.find(" ", rank_start)  # 랭킹 숫자 이후 위치 찾기
        global_rank = meta_description[rank_start:rank_end]
        return int(global_rank.replace(',', ''))
    except (AttributeError, TypeError, KeyError):
        return None

def get_raw_word_count(url: str):
    try:
        words = count_words(url)
        return [len(words)]
    except Exception:
        return [0]

def get_brand_check_for_domain(url: str):
    try:
        domain = urllib.parse.urlparse(url).netloc
        if is_brand_name(domain.split('.')[0]):
            return [1]
        return [0]
    except Exception:
        return [0]

def get_average_word_length(url: str):
    try:
        words = count_words(url)
        if words:
            return [sum(len(word) for word in words) / len(words)]
        return [0]
    except Exception:
        return [0]

def get_longest_word_length(url: str):
    try:
        words = count_words(url)
        if words:
            return [max(len(word) for word in words)]
        return [0]
    except Exception:
        return [0]

def get_shortest_word_length(url: str):
    try:
        words = count_words(url)
        if words:
            return [min(len(word) for word in words)]
        return [0]
    except Exception:
        return [0]

def get_standard_deviation(url: str):
    try:
        words = count_words(url)
        if words:
            lengths = [len(word) for word in words]
            return [statistics.stdev(lengths) if len(lengths) > 1 else 0]
        return [0]
    except Exception:
        return [0]

def get_adjacent_word_count(url: str):
    try:
        words = count_words(url)
        adjacent_count = sum(1 for i in range(1, len(words)) if len(words[i]) == len(words[i-1]))
        return [adjacent_count]
    except Exception:
        return [0]

def get_average_adjacent_word_length(url: str):
    try:
        words = count_words(url)
        adjacent_lengths = [len(words[i]) for i in range(1, len(words)) if len(words[i]) == len(words[i-1])]
        if adjacent_lengths:
            return [sum(adjacent_lengths) / len(adjacent_lengths)]
        return [0]
    except Exception:
        return [0]

def get_separated_word_count(url: str):
    try:
        words = count_words(url)
        return [sum(1 for word in words if '-' in word or '_' in word)]
    except Exception:
        return [0]

def get_keyword_count(url: str):
    try:
        page_content = get_page_content(url)
        keywords = read_file_to_list('keywords.txt')
        return [sum(page_content.lower().count(keyword) for keyword in keywords)]
    except Exception:
        return [0]

def get_brand_name_count(url: str):
    try:
        words = count_words(url)
        return [sum(1 for word in words if is_brand_name(word))]
    except Exception:
        return [0]

def get_similar_keyword_count(url: str):
    try:
        page_content = get_page_content(url)
        keywords = ["login", "bank", "secure", "account", "update"]
        similar_keywords = 0
        for keyword in keywords:
            words = page_content.split()
            for word in words:
                if fuzz.partial_ratio(keyword, word) > 80:  # Threshold for similarity
                    similar_keywords += 1
        return [similar_keywords]
    except Exception:
        return [0]

def get_similar_brand_name_count(url: str):
    try:
        return get_brand_name_count(url)
    except Exception:
        return [0]

def get_random_word_count(url: str):
    try:
        words = count_words(url)
        return [sum(1 for word in words if not is_brand_name(word) and not re.match(r'^[a-zA-Z0-9]+$', word))]
    except Exception:
        return [0]

def get_target_brand_name_count(url: str):
    try:
        return get_brand_check_for_domain(url)
    except Exception:
        return [0]

def get_target_keyword_count(url: str):
    try:
        return get_keyword_count(url)
    except Exception:
        return [0]

def get_other_words_count(url: str):
    try:
        words = count_words(url)
        english_words = set(['computer', 'pencil', 'notebook'])  # Placeholder for a larger dictionary
        return [sum(1 for word in words if word in english_words)]
    except Exception:
        return [0]

def get_digit_count(url: str):
    try:
        return [sum(c.isdigit() for c in url)]
    except Exception:
        return [0]

def get_subdomain_count(url: str):
    try:
        subdomain = urllib.parse.urlparse(url).netloc.split('.')
        return [len(subdomain) - 2]
    except Exception:
        return [0]

def get_random_domain(url: str):
    try:
        return get_random_word_count(url)
    except Exception:
        return [0]

def get_length(url: str):
    try:
        parsed_url = urllib.parse.urlparse(url)
        return [len(parsed_url.netloc), len(parsed_url.path), len(url)]
    except Exception:
        return [0, 0, 0]

def get_known_tld(url: str):
    try:
        tlds = [".com", ".org", ".net", ".info", ".biz", ".gov", ".edu"]
        for tld in tlds:
            if url.endswith(tld):
                return [1]
        return [0]
    except Exception:
        return [0]

def get_www_com(url: str):
    try:
        return [1 if "www." in url else 0, 1 if ".com" in url else 0]
    except Exception:
        return [0, 0]

def get_punny_code(url: str):
    try:
        return [1 if "xn--" in url else 0]
    except Exception:
        return [0]

def get_special_character(url: str):
    try:
        special_characters = ['-', '.', '/', '@', '?', '&', '=', '_']
        return [url.count(char) for char in special_characters]
    except Exception:
        return [0] * 8

def get_consecutive_character_repeat(url: str):
    try:
        return [max([len(match.group(0)) for match in re.finditer(r'(.)\1*', url)])]
    except Exception:
        return [0]

def get_global_rank_check(url: str):
    try:
        domain = urllib.parse.urlparse(url).netloc
        rank = get_global_rank_from_meta(domain)

        if rank:
            return [1 if rank <= 1000000 else 0, rank]
        else:
            return [0, rank]
    except Exception as e:
        print(f"Error: {e}")
        return [0, 4,294,967,296]

class Get_URL_Feature:
    def __init__(self, url: str):
        self.raw_word_count = get_raw_word_count(url)
        self.brand_check_for_domain = get_brand_check_for_domain(url)
        self.average_word_length = get_average_word_length(url)
        self.longest_word_length = get_longest_word_length(url)
        self.shortest_word_length = get_shortest_word_length(url)
        self.standard_deviation = get_standard_deviation(url)
        self.adjacent_word_count = get_adjacent_word_count(url)
        self.average_adjacent_word_length = get_average_adjacent_word_length(url)
        self.separated_word_count = get_separated_word_count(url)
        self.keyword_count = get_keyword_count(url)
        self.brand_name_count = get_brand_name_count(url)
        self.similar_keyword_count = gets_similar_keyword_count(url)
        self.similar_brand_name_count = get_similar_brand_name_count(url)
        self.random_word_count = get_random_word_count(url)
        self.target_brand_name_count = get_target_brand_name_count(url)
        self.target_keyword_count = get_target_keyword_count(url)
        self.other_words_count = get_other_words_count(url)
        self.digit_count = get_digit_count(url)
        self.subdomain_count = get_subdomain_count(url)
        self.random_domain = get_random_domain(url)
        self.length = get_length(url)
        self.known_tld = get_known_tld(url)
        self.www_com = get_www_com(url)
        self.punny_code = get_punny_code(url)
        self.special_character = get_special_character(url)
        self.consecutive_character_repeat = get_consecutive_character_repeat(url)
        self.global_rank_check = get_global_rank_check(url)

        self.feature = []
        self.feature.extend(self.raw_word_count)
        self.feature.extend(self.brand_check_for_domain)
        self.feature.extend(self.average_word_length)
        self.feature.extend(self.longest_word_length)
        self.feature.extend(self.shortest_word_length)
        self.feature.extend(self.standard_deviation)
        self.feature.extend(self.adjacent_word_count)
        self.feature.extend(self.average_adjacent_word_length)
        self.feature.extend(self.separated_word_count)
        self.feature.extend(self.keyword_count)
        self.feature.extend(self.brand_name_count)
        self.feature.extend(self.similar_keyword_count)
        self.feature.extend(self.similar_brand_name_count)
        self.feature.extend(self.random_word_count)
        self.feature.extend(self.target_brand_name_count)
        self.feature.extend(self.target_keyword_count)
        self.feature.extend(self.other_words_count)
        self.feature.extend(self.digit_count)
        self.feature.extend(self.subdomain_count)
        self.feature.extend(self.random_domain)
        self.feature.extend(self.length)
        self.feature.extend(self.known_tld)
        self.feature.extend(self.www_com)
        self.feature.extend(self.punny_code)
        self.feature.extend(self.special_character)
        self.feature.extend(self.consecutive_character_repeat)
        self.feature.extend(self.global_rank_check)

# Example usage
url = "http://www.example.com/path/to/resource"
features = Get_URL_Feature(url)
print(features.feature)
