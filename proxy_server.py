from fastapi import FastAPI, Request
import os
from openai import OpenAI

app = FastAPI()

# تست سلامت سرور
@app.get("/")
def root():
    return {"status": "ok"}

# مسیر اصلی چت
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not user_message:
        return {"reply": "پیام خالی ارسال شد."}

    try:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "تو یک دستیار فارسی هستی."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        return {"reply": reply}

    except Exception as e:
        return {"reply": f"خطا در سرور: {str(e)}"}
