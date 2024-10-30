from . import google_crawler
from db.database_settings import DatabaseSettings
from .ai_generator import TextGenerator
from .wp_publish import WordpressPublish
import time


class StartBot:
    def __init__(self, api_key=None, model_engine=None):
        self.settings = DatabaseSettings()
        self.datas = self.settings.get_all_data("settings")
        self.generator = TextGenerator(api_key=api_key, model_engine=model_engine)
        if self.datas is not None:
            self.api_key = self.datas[0].api_key
            self.wp_api_url = self.datas[0].wp_api_url
            self.wp_username = self.datas[0].wp_username
            self.wp_password = self.datas[0].wp_password
            self.sleep_time = self.datas[0].sleep_time
            self.max_length = self.datas[0].max_length

    def crawl(self):
        google_crawler.open_keywords()
        
    def generate_title(self, keyword):
        prompt = ', '.join(keyword.split())
        main_key = "Generate a blog title with the following keywords: " + prompt
        return self.generator.generate_text(prompt=main_key, max_tokens=int(self.max_length))

    def post(self, keyword, title):
        blog_introduction = "Generate a blog introduction with the following title:" + title
        intro = self.generator.generate_text(prompt=blog_introduction, max_tokens=int(self.max_length))
        sub_key = "Generate a minimum 3 subtitles with the following keywords:" + title
        sub_titles = self.generator.generate_text(prompt=sub_key, max_tokens=int(self.max_length))
        blog_text = "Generate a blog article with the following subtitles: \n Note: Write the subtitles within the article and place them within an h2 tag while placing the paragraphs within a p tag." + sub_titles
        text = self.generator.generate_text(prompt=blog_text, max_tokens=int(self.max_length))
        blog_content = intro + " " + text
        wp_publish = WordpressPublish(api_url=self.wp_api_url, username=self.wp_username, password=self.wp_password, title=title, article=blog_content)
        wp_publish.publish()
        self.settings.delete_one_suggestion(suggestion=keyword)
        time.sleep(int(self.sleep_time))
