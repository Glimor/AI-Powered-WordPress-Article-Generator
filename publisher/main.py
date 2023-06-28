from . import google_crawler
from db.database_settings import DatabaseSettings
from .ai_generator import TextGenerator
from .wp_publish import WordpressPublish
import time
from db.config import Config


class StartBot:
    def __init__(self, main_dialog):
        self.settings = DatabaseSettings()
        self.datas = self.settings.get_all_data("settings")
        self.main_dialog = main_dialog
        if self.datas is not None:
            self.api_key = self.datas[0][1]
            self.wp_api_url = self.datas[0][2]
            self.wp_username = self.datas[0][3]
            self.wp_password = self.datas[0][4]
            self.sleep_time = self.datas[0][5]
            self.max_length = self.datas[0][6]

    def crawl(self):
        google_crawler.open_keywords()

    def generate(self):
        keywords = self.settings.get_all_data("suggestions")
        for keyword in keywords:
            Config.article_counter += 1
            self.main_dialog.label_4.setText(str(Config.article_counter))
            self.main_dialog.label_4.repaint()
            self.post(keyword[1])

    def post(self, keyword):
        text_generator = TextGenerator(api_key=self.api_key, model_engine="text-davinci-003")
        prompt = ', '.join(keyword.split())
        print("Google Trends: " + prompt)
        main_key = "Generate a blog title with the following keywords: " + prompt
        title = text_generator.generate_text(prompt=main_key, max_tokens=int(self.max_length))
        print("Title Generated: ", title)
        blog_introduction = "Generate a blog introduction with the following title:" + title
        intro = text_generator.generate_text(prompt=blog_introduction, max_tokens=int(self.max_length))
        sub_key = "Generate a minimum 3 subtitles with the following keywords:" + title
        sub_titles = text_generator.generate_text(prompt=sub_key, max_tokens=int(self.max_length))
        print("Subtitles Generated: " + sub_titles)
        blog_text = "Generate a blog article with the following subtitles: \n Note: Write the subtitles within the article and place them within an h2 tag while placing the paragraphs within a p tag." + sub_titles
        text = text_generator.generate_text(prompt=blog_text, max_tokens=int(self.max_length))
        blog_content = intro + " " + text
        wp_publish = WordpressPublish(api_url=self.wp_api_url, username=self.wp_username, password=self.wp_password, title=title, article=blog_content)
        wp_publish.publish()
        print("Article Published for: " + title)
        print("Sleeping for " + self.sleep_time + " seconds")
        self.settings.delete_one_suggestion(suggestion=keyword)
        time.sleep(int(self.sleep_time))
