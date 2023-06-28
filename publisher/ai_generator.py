import openai

openai.api_key = ""
model_engine = "text-davinci-003"

class TextGenerator:
    def __init__(self, api_key, model_engine):
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key

    def generate_text(self, prompt, max_tokens, stop=None, temperature=0.8):
        completions = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=stop,
            temperature=temperature,
        )

        text = completions["choices"][0]["text"]


        return text