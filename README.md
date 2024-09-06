
# 📝 AI-Powered WordPress Article Generator 🚀

## 🔄 Version 1.1.0 Updates
- 🌍 **German Language Support:** Now supports article generation in German.
- 🧠 **Automatic Language Detection:** Detects the language based on input and adjusts article generation accordingly.
- 🔑 **Multiple Keyword Support:** Generate articles based on a set of keywords for improved relevance.
- 💻 **User-Friendly Interface:** Graphical User Interface (GUI) added for seamless user experience.

## 🖼️ Application Screenshots
![Settings Screen](https://i.imghippo.com/files/fBq321725657886.png)
![Main Screen](https://i.ibb.co/9cPm5MG/Screenshot-2024-09-07-001810.png)


## ⭐ Key Features
- 🤖 **AI-Powered Article Generation:** Automatically generates articles using OpenAI's GPT AI based on user-provided keywords.
- 🖱️ **Easy-to-Use GUI:** Intuitive graphical interface for non-technical users.
- 🔍 **SEO Optimization:** Uses Google keyword search to align generated articles with trending topics.
- 📰 **Auto WordPress Publishing:** Automatically publishes generated articles to your WordPress site.

## ⚙️ Prerequisites
Ensure you have the following details ready to configure the application:
- 🔑 **OPENAI_API_KEY:** Your API Key from OpenAI.
- 🔗 **WP_API_URL:** The API URL of your WordPress site.
- 👤 **WP_USERNAME:** Your WordPress username.
- 🔒 **WP_PASSWORD:** Your WordPress password.

## 🛠️ Configuration
To set up, start the `main.py` file and update the following settings:
```python
OPENAI_API_KEY = "Your OpenAI API Key"
WP_API_URL = "Your WordPress API URL"
WP_USERNAME = "Your WordPress Username"
WP_PASSWORD = "Your WordPress Password"
SLEEP_TIME = "Wait time between each post publication"
MAX_LENGTH = "Maximum length of articles in words"
```

## 🚀 How It Works
1. 🔍 **Google Search:** The script starts by performing a Google search for relevant keywords based on the user input.
2. 📝 **AI Article Generation:** The retrieved keywords are used as a base for GPT to generate articles.
3. 📤 **Auto-Publishing:** These AI-generated articles are automatically published to your WordPress site, with a defined time interval between posts.

## 💡 Usage
Add your suggestions (keywords) in the main screen and run the script with the following command:

```bash
python main.py
```

🔧 **Tip:** Adjust the `sleep_time` and `max_length` settings to meet your preferences and WordPress API rate limits.

## ⚠️ Disclaimer
This project is for educational purposes. Please ensure it complies with OpenAI's usage policies and WordPress's terms of service.

🌟 **Enjoy automating your article creation and exploring the potential of AI in content generation!**

## Support the Project

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/glimor)
