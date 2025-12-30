import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from prompts import SYSTEM_PROMPT, build_user_prompt

# Load environment variables
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Load company info
with open("company_info.txt", "r", encoding="utf-8") as f:
    company_context = f.read()

def ask_bot(question):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": build_user_prompt(question, company_context)
            }
        ],
        temperature=0.2  # Low temperature = less hallucination
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("ZeniPay Technologies Support Bot (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break
        answer = ask_bot(user_input)
        print(f"Bot: {answer}")
