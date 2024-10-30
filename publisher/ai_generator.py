from openai import OpenAI
import sys


api_key = ""

class TextGenerator:
    def __init__(self, api_key, model_engine="text-davinci-003"):
        self.api_key = api_key
        self.model_engine = model_engine
        self.client = OpenAI(
            api_key=api_key
        )

    def generate_text(self, prompt, max_tokens, stop=None, temperature=0.7):
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user", 
                        "content": prompt
                    },
                ],
                model=self.model_engine,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop
            )
            
            try:
                text = completion['choices'][0]['message']['content'].strip()
                return text
            except:
                print("Please fix code on the 'generate_text' method. Unable to extract text from response.")
        
        except Exception as e:
            print(e.body['message'])
            sys.exit(1)
        