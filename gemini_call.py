from dotenv import load_dotenv
import os, json, requests


load_dotenv()




def gemini_request( prompt):
    try:

        api_key     =os.getenv('GEMINI_API_KEY')        

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 1,
                "topK": 64,
                "topP": 0.95,
                "maxOutputTokens": 8192,
                "responseMimeType": "application/json"
            }

        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        response = response.json()

        data = response.get('candidates')[0].get('content').get('parts')[0].get('text').strip()

        final_response = clean_and_format_response(data) or {}

        return final_response
    except Exception as e:
        print("Exception in geminie:", e ,flush= True)
        return {"error": str(e)}
    

def clean_and_format_response(response):
    try:
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        json_str = response[json_start:json_end]
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        print("Error decoding JSON:", e ,flush= True)
        return None


print(gemini_request("What are the benefits of LLM"))