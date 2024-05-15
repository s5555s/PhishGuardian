def get_raw_word_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_brand_check_for_domain(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_average_word_length(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_longest_word_length(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_shortest_word_length(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_standard_deviation(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_adjacent_word_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_average_adjacent_word_length(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_separated_word_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_keyword_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_brand_name_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_similar_brand_name_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_random_word_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_target_brand_name_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_target_keyword_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_other_words_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_digit_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_subdomain_count(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_random_domain(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_length(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_known_tld(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_www_com(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_punny_code(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_special_character(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_consecutive_character_repeat(url: str):
    {
        try:
            return 0
        except:
            return 0
    }
def get_alexa_check(url: str):
    {
        try:
            return 0
        except:
            return 0
    }





class Get_URL_Feature:
    def __init__(self, url: str)
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
        self.alexa_check = get_alexa_check(url)
        self.raw_word_count
        self.feature = []
        self.feature.extend(
            self.raw_word_count, 
            self.brand_check_for_domain, 
            self.average_word_length, 
            self.longest_word_length, 
            self.shortest_word_length, 
            self.standard_deviation, 
            self.adjacent_word_count, 
            self.average_adjacent_word_length, 
            self.separated_word_count, 
            self.keyword_count, 
            self.brand_name_count, 
            self.similar_brand_name_count, 
            self.random_word_count, 
            self.target_brand_name_count, 
            self.target_keyword_count, 
            self.other_words_count, 
            self.digit_count, 
            self.subdomain_count, 
            self.random_domain, 
            self.length, 
            self.known_tld, 
            self.www_com, 
            self.punny_code, 
            self.special_character, 
            self.consecutive_character_repeat, 
            self.alexa_check
        )
        
