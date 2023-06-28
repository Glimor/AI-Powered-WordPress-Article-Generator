import requests, json
import langdetect
from db.database_settings import DatabaseSettings
class GoogleCrawler:
    def __init__(self, keyword):
        accept_language = langdetect.detect(keyword)
        self.keyword = keyword
        self.headers = {
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
        self.url = 'http://google.com/complete/search?client=chrome&q=' + self.keyword
        self.settings = DatabaseSettings()

    def get_suggestions(self):
        response = requests.get(self.url, headers=self.headers)
        json_data = json.loads(response.text)
        suggestions = json_data[1]
        return suggestions

    def write_suggestions(self):
        suggestions = self.get_suggestions()
        for suggestion in suggestions:
            self.settings.insert_suggestion(suggestion=suggestion)


def open_keywords():
    settings = DatabaseSettings()
    keywords = settings.get_all_data("keywords")
    for keyword in keywords:
        print(keyword[1])
        google_crawler = GoogleCrawler(keyword=keyword[1])
        google_crawler.write_suggestions()
        settings.delete_one_keyword(keyword=keyword[1])