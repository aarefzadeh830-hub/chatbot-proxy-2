# proxy/proxy_server.py
from fastapi import FastAPI, Request
import requests, os

app = FastAPI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

@app.get('/')
async def home():
    return {'status':'ok'}

@app.post('/chat')
async def chat(request: Request):
    body = await request.json()
    user_message = body.get('message', '')
    model = body.get('model', 'gpt-3.5-turbo')
    max_length = int(body.get('max_length', 200))

    if not OPENAI_API_KEY:
        return {'error':'Server missing OPENAI_API_KEY'} , 500

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': model,
        'messages': [{'role':'user','content': user_message}],
        'max_tokens': max_length
    }

    resp = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data, timeout=60)
    try:
        return resp.json()
    except Exception:
        return {'error': 'invalid response from upstream', 'text': resp.text}
