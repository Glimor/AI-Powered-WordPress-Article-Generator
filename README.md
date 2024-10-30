
# 📝 AI-Powered WordPress Article Generator 🚀

## 🔄 Version 2.0.0 Updates
- 🆕 **Modern CLI Interface Added:** A modern Command Line Interface (CLI) has replaced the previous GUI, enabling full control via CLI.
- ⚙️ **Full Configuration through CLI:** All settings and configurations are now managed through CLI options for streamlined setup.
- 🎛️ **Interactive Menu with 4 Options:** Upon running `main.py` or `GlimorWp.exe`, an interactive menu with the following options is displayed:
    - **Option 1:** Configure bot settings, such as OpenAI API key and model selection.
    - **Option 2:** Add keywords manually or import from a `.txt` file (1 keyword per line).
    - **Option 3:** Start the bot for automated article generation.
    - **Option 4:** Monitor bot progress directly via CLI.

- 🤖 **AI Model Selection Feature:** Now supports selection of AI models (e.g., `gpt-4o-mini`, `gpt-4o`, etc.) to customize generation.
- 🛠️ **Improved Database Query Handling:** Enhanced database querying for optimized performance.

## 🖼️ Application Screenshots
<img src="https://i.ibb.co/TYJdNTb/Screenshot-2024-10-30-234102.png" alt="Screen" width="300px">

## ⭐ Key Features
- 🤖 **AI-Powered Article Generation:** Automatically generates articles using OpenAI's GPT AI based on user-provided keywords.
- 🔧 **Modern CLI Interface:** Intuitive CLI for quick setup and efficient use.
- 🔍 **SEO Optimization:** Uses Google keyword search to align generated articles with trending topics.
- 📰 **Auto WordPress Publishing:** Automatically publishes generated articles to your WordPress site.

## ⚙️ Prerequisites
Ensure you have the following details ready to configure the application:
- 🔑 **OPENAI_API_KEY:** Your API Key from OpenAI.
- 🔗 **WP_API_URL:** The API URL of your WordPress site.
- 👤 **WP_USERNAME:** Your WordPress username.
- 🔒 **WP_PASSWORD:** Your WordPress password.

## 🛠️ Configuration
To set up, start the `main.py` file or `GlimorWp.exe` executable, then select **Option 1** from the CLI menu to configure the following settings:
```python
Your OpenAI API Key
Your WordPress Username
Your WordPress Password
Your WordPress API URL
Wait time between each post publication
Maximum length of articles in words
Preferred model (gpt-4o / gpt-4o-mini)
Maximum number of articles to generate
```

## 🚀 How It Works
1. 🔍 **Google Search:** The script starts by performing a Google search for relevant keywords based on the user input.
2. 📝 **AI Article Generation:** The retrieved keywords are used as a base for GPT to generate articles.
3. 📤 **Auto-Publishing:** These AI-generated articles are automatically published to your WordPress site, with a defined time interval between posts.

## 💡 Usage
To add keywords, either input them directly or load from a `.txt` file (1 keyword per line) using **Option 2** from the CLI menu. Run the script with the following command:

```bash
python main.py
```

🔧 **Tip:** Adjust the `sleep_time` and `max_length` settings to meet your preferences and WordPress API rate limits.

## ⚠️ Disclaimer
This project is for educational purposes. Please ensure it complies with OpenAI's usage policies and WordPress's terms of service.

🌟 **Enjoy automating your article creation and exploring the potential of AI in content generation!**

## Support the Project

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/glimor)
