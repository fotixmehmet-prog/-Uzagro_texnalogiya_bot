import asyncio
import requests
from aiogram import Bot, Dispatcher, types, F
from flask import Flask
from threading import Thread
import os

# --- TOKENLAR ---
TG_TOKEN = "8731206134:AAEgFuDAiyUCMsyK1XWRsFQc54RHpTqWbAw"
GEMINI_KEY = "AIzaSyCGxNtX7SBwJDb3whBocgMN-TFgrvr052U"

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
app = Flask('')

@app.route('/')
def home():
    return "Bot is live!"

def run():
    # Render serveri uchun port sozlamasi
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def ask_gemini(text):
    # Google Gemini API (v1beta versiyasi)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    try:
        res = requests.post(url, json={"contents": [{"parts": [{"text": text}]}]}, timeout=30)
        return res.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "⚠️ Google API ulanishda xato berdi!"

@dp.message(F.text)
async def handle(msg: types.Message):
    await bot.send_chat_action(msg.chat.id, "typing")
    answer = ask_gemini(msg.text)
    await message.reply(answer)

async def main():
    # Flask serverni alohida oqimda yurgizish (Render uchun)
    Thread(target=run).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
