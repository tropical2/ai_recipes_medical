import openai_integration
import page_parser

MAX_CHAR_LENGTH_OUTREACH_TARGET = 1000
MAX_CHAR_LENGTH_LINK_TARGET = 500


# if over limit, keep a part at the beginning and at the end of the string. Usually intro and summary are where the article contains the most dense information.
def truncate_input(string, limit):
    if len(string) <= limit:
        return string

    beginning_ratio = 2 / 3
    end_ratio = 1 / 3

    beginning_length = int(limit * beginning_ratio)
    end_length = limit - beginning_length

    beginning = string[:beginning_length]
    end = string[-end_length:]

    return beginning + end

def build_prompt(outreach_content, link_target_content):
    base_prompt = "I am pasting you two articles. The first, named OutreachTarget is the article of the website that we are contacting. The second, named LinkTarget is the article that we want to get a backlink from. It is possible that the original articles are too long for you to process. That is why we will preprocess the article if it is too long and only send you the beginning and the end of the articles. However, those parts of the article probably will contain the most dense information and provide you with sufficient context. Do not confuse those two articles with each other. Next I am sending the articles."
    final_prompt = base_prompt + "OutreachTarget: " + outreach_content + "This was the end of the OutreachTarget text. Next comes the LinkTarget text: " + link_target_content
    return final_prompt

def process_request(outreach_target, link_target):
    outreach_content = page_parser.parse(outreach_target)
    outreach_content = truncate_input(outreach_content, MAX_CHAR_LENGTH_OUTREACH_TARGET)
    link_target_content = page_parser.parse(link_target)
    link_target_content = truncate_input(link_target_content, MAX_CHAR_LENGTH_LINK_TARGET)

    gpt_api = openai_integration.GptApi()
    prompt = build_prompt(outreach_content, link_target_content)
    ai_answer = gpt_api.send(prompt)
    return ai_answer

if __name__ == "__main__":
    link_target = "https://www.refluxgate.de/sodbrennen"
    outreach_target = "https://www.sodbrennen.de/ursachen-sodbrennen/"

    answer = process_request(outreach_target, link_target)
    print(answer)