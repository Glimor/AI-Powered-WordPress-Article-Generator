import requests, json
import langdetect
from db.database_settings import DatabaseSettings
class GoogleCrawler:
    def __init__(self):
        self.settings = DatabaseSettings()
        
    def crawl(self, keyword):
        accept_language = langdetect.detect(keyword)
        keyword = keyword
        headers = {
            "authority": "google.com",
            "method": "GET",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "accept": "*/*",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://google.com/",
            "accept-language": accept_language,
        }
        url = 'http://google.com/complete/search?client=chrome&q=' + keyword
        response = requests.get(url, headers=headers)
        json_data = json.loads(response.text)
        suggestions = json_data[1]
        return suggestions

    def write_suggestions(self, keyword):
        suggestions = self.crawl(keyword)
        for suggestion in suggestions:
            self.settings.insert_suggestion(suggestion=suggestion, keyword=keyword)


def open_keywords():
    settings = DatabaseSettings()
    crawler = GoogleCrawler()
    keywords = settings.get_all_data("keywords")
    for keyword in keywords:
        try:
            crawler.crawl(keyword=keyword.keyword)
            crawler.write_suggestions(keyword=keyword.keyword)
            settings.delete_one_keyword(keyword=keyword.keyword)
        except:
            continue