### Integrate OpenAI 
It is a simple repo to call OpenAI for any query.

First of all install the requirements
```
pip3 install -r requirements.txt
```

Then create a .env file in the folder and place your OpenAI API key 
```
OPENAI_API_KEY="YOUR OPENAI API KEY"
```

now simple update the prompt in the openai_call file and run the file using  `python openai_call.py`



## How to create OpenAI API Key
- Go to [open ai playground](https://platform.openai.com/docs/overview)
- If your account is already logged in you'll be at documentation page else first login to your gpt account
- Then click on the profile icon on top right corner and in dropdown click on `your profile` tab
- Now you'll be on your profile setting tab
- Here you'll see a tab named as `User API Keys (Legacy)` click this
- You will see an option to create An API key.
- Create API Key and place that key in .env file in the project