import openai
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY ,flush= True)
openai.api_key = OPENAI_API_KEY

GPT_TIMEOUT=20

def openai_request( prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=GPT_TIMEOUT
        ) 

        data = response['choices'][0]['message']['content'].strip()

        print(data)
    except Exception as e:
        print("Exception in openai_request:", e ,flush= True)
        return {"error": str(e)}


openai_request("What are the benefits of LLM")