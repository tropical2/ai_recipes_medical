import openai

with open("keys/openai", "r") as f:
    openai.api_key = f.readline()


class GptApi:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.set_system_message = "You are a helpful assistant."

    def set_new_system_message(self, message):
        self.set_system_message = message
        return

    def send(self, prompt):
        messages = [
            {"role": "assistant", "content": self.set_system_message},
            {"role": "user", "content": prompt},
        ]
        completion = openai.ChatCompletion.create(model=self.model, messages=messages)
        reply = completion.choices[0].message.content
        return reply


if __name__ == '__main__':
    api = GptApi()
    reply = api.send("create a recipe for GERD")
    print(reply)

