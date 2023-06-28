import requests, json

class WordpressPublish:
    def __init__(self, api_url, username, password, title, article):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.title = title
        self.article = article

    def publish(self):
        data = {
            "title": self.title,
            "content": self.article,
            "status": "publish",
        }
        response = requests.post(
            self.api_url,
            auth=(self.username, self.password),
            json=data,
        )
        json_data = json.loads(response.text)
        return json_data