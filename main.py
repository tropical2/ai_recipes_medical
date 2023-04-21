import openai_integration


def build_prompt(disease, language="English"):
    if disease == "GERD":
        disease_prompt = "Provide a fitting recipe for a patient with gastroesophageal reflux."
    else:
        disease_prompt = "Provide a fitting recipe for a patient with " + disease + "."

    language_prompt = "The patient speaks " + language + "." + " Therefore provide the recipe in native level " + language + "."
    return disease_prompt + " " + language_prompt


def process_request(disease, language="English"):
    gpt_api = openai_integration.GptApi()
    gpt_api.set_system_message = "You are a a highly skilled dietician who recommends patients fitting but tasty recipes to help relief symptoms of their disease. You will be given the specific disease that the recipe is supposed to help with. You may or may not be given additional contraints to fulfill. Additionally to the recipe, provide a explanation why this recipe is good for a specific disease. Do not talk about yourself, only provide the recipes and other requested information."
    prompt = build_prompt(disease, language)
    ai_answer = gpt_api.send(prompt)
    return ai_answer


if __name__ == "__main__":

    disease = "SIBO"
    answer = process_request(disease)
    print(answer)