import openai

with open("keys/openai", "r") as f:
    openai.api_key = f.readline()


class GptApi:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.set_system_message = "You are a Digital PR specialist. Your job is to generate backlinks by reaching out to website owners. Write a message that is innovative. Dont be boring. Be specific about why we reach out specifically for this piece of content that the website owner published and why it fits to our content. Most important, avoid writing the email like a typical outreach email. We want to stand out. Write the email in German. Dont be uptight. Be informal. Write the email in German. You have native level German skills."
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
    reply = api.send("reach out to the owner of the site refluxgate.com and ask them to link to my site")
    print(reply)

