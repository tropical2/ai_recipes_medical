import openai
import logging

logger = logging.getLogger()

with open("keys/openai", "r") as f:
    openai.api_key = f.readline()


class GptApi:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.set_system_message = "You are a helpful assistant."

    def set_new_system_message(self, message):
        logger.debug('Setting new system message')
        self.set_system_message = message
        return

    def send(self, prompt):
        messages = [
            {"role": "assistant", "content": self.set_system_message},
            {"role": "user", "content": prompt},
        ]
        logger.debug('Sending request to OpenAI')

        max_retries = 3
        current_retries = 0
        success = False
        while max_retries >= current_retries:
            try:
                completion = openai.ChatCompletion.create(model=self.model, messages=messages)
                success = True
                break
            except openai.error.RateLimitError as e:
                logger.warning('OpenAI API is overloaded')
                logger.warning(e)
                current_retries += 1
                continue
            except Exception as e:
                logger.critical('Unhandled OpenAI API error occurred')
                logger.critical(e)
                continue

        if success:
            reply = completion.choices[0].message.content
        else:
            reply = "Sorry, I am currently overloaded with requests. Please try again later."
            logger.warning('Limit of unsuccessfully requests to OpenAI reached')
        return reply


if __name__ == '__main__':
    api = GptApi()
    reply = api.send("create a recipe for GERD")
    print(reply)

