
# AI-Powered WordPress Article Generator  
  
## Update Notes (1.1.0)  
- Added support for German language.  
- Added support auto language detection.  
- Added support for multiple keywords.  
- Added GUI for easy usage.  

## Images
![Settings Screen](https://www.linkpicture.com/q/1_232.png)

![Main Screen](https://www.linkpicture.com/q/2_90.png)
  
## Features  
  
- Auto-generates articles with GPT AI.  
- GUI for easy usage  
- Performs keyword searches on Google to align with relevant topics.  
- Automatically publishes articles to your WordPress site.  
  
## Prerequisites  
  
Ensure you have the following details at hand:  
  
- OPENAI_API_KEY: Your API Key obtained from OpenAI.  
- WP_API_URL: Your WordPress API URL.  
- WP_USERNAME: Your WordPress username.  
- WP_PASSWORD: Your WordPress password.  
  
## Configuration  
  
Start main.py and update the following parameters:  
  
OPENAI_API_KEY = "Your OpenAI API Key"  
WP_API_URL = "Your WordPress API URL"  
WP_USERNAME = "Your WordPress Username"  
WP_PASSWORD = "Your WordPress Password"  
SLEEP_TIME = "Wait time between each post publication"  
MAX_LENGTH = "Maximum length of articles in words"  
  
## How it works  
  
1. The script starts by searching on Google for relevant keywords based on the provided input.  
2. The obtained keywords are used as a base for the AI to generate articles.  
3. These articles are automatically published to your WordPress site with a defined sleep time in between each post.  
  
## Usage  
Add your suggestions (keywords) in the "suggestions_de.txt" or "suggestions_en.txt" file. The script will automatically use these keywords to generate articles.  
Run the script by executing the following command:  
  
python main.py  
  
**Note:** Adjust the sleep time and maximum length of the articles according to your preferences and usage limits.  
  
## Donations with Crypto (Optional)  
- BTC: 0xb0dcc1ed951eca351720064eb7399efaa148a714 (BEP20)  
- ETH: 0xb0dcc1ed951eca351720064eb7399efaa148a714 (BEP20)  
- USDT: TNZYwR8sVeVyg1taNcJxe2yTxsuRxnk6iK (TRC20)  
  
## Disclaimer  
  
This project is for educational purposes. Please use it responsibly and ensure it complies with OpenAI's use-case policy and WordPress's terms of service.  
  
Enjoy automating your article generation process and explore the power of AI in content creation!