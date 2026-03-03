import asyncio
import logging
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, F
from threading import Thread

# 1. Sozlamalar (O'zingizning API kalitlarni qo'ying)
API_TOKEN = 'BOT_TOKENINGIZ_BU_YERGA'
GOOGLE_API_KEY = 'GEMINI_API_KEY_BU_YERGA'

# Gemini konfiguratsiyasi
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Bot va Dispatcher obyektlari
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 2. Gemini bilan asinxron muloqot funksiyasi
async def ask_gemini(prompt):
    try:
        # generate_content_async - bu asinxron kutish imkonini beradi
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Google API ulanishda xato: {str(e)}"

# 3. Xabarlarni qabul qilish (Handle)
@dp.message(F.text)
async def handle(msg: types.Message):
    # Bot "yozmoqda..." holatini ko'rsatadi
    await bot.send_chat_action(msg.chat.id, "typing")
    
    # Gemini'dan javobni asinxron kutamiz (await muhim!)
    answer = await ask_gemini(msg.text)
    
    # Foydalanuvchiga javob qaytaramiz
    await msg.reply(answer)

# 4. Qo'shimcha funksiya (agar Thread kerak bo'lsa)
def run():
    print("Qo'shimcha Thread ishga tushdi...")

# 5. Asosiy ishga tushirish qismi
async def main():
    # Loggingni yoqish (xatolarni ko'rish uchun)
    logging.basicConfig(level=logging.INFO)
    
    # Threadni ishga tushirish (agar rasmda ko'rsatganingizdek kerak bo'lsa)
    Thread(target=run).start()
    
    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi!")
        import asyncio
import logging
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, F
from threading import Thread

# 1. Sozlamalar (O'zingizning API kalitlarni qo'ying)
API_TOKEN = 'BOT_TOKENINGIZ_BU_YERGA'
GOOGLE_API_KEY = 'GEMINI_API_KEY_BU_YERGA'

# Gemini konfiguratsiyasi
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Bot va Dispatcher obyektlari
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 2. Gemini bilan asinxron muloqot funksiyasi
async def ask_gemini(prompt):
    try:
        # generate_content_async - bu asinxron kutish imkonini beradi
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Google API ulanishda xato: {str(e)}"

# 3. Xabarlarni qabul qilish (Handle)
@dp.message(F.text)
async def handle(msg: types.Message):
    # Bot "yozmoqda..." holatini ko'rsatadi
    await bot.send_chat_action(msg.chat.id, "typing")
    
    # Gemini'dan javobni asinxron kutamiz (await muhim!)
    answer = await ask_gemini(msg.text)
    
    # Foydalanuvchiga javob qaytaramiz
    await msg.reply(answer)

# 4. Qo'shimcha funksiya (agar Thread kerak bo'lsa)
def run():
    print("Qo'shimcha Thread ishga tushdi...")

# 5. Asosiy ishga tushirish qismi
async def main():
    # Loggingni yoqish (xatolarni ko'rish uchun)
    logging.basicConfig(level=logging.INFO)
    
    # Threadni ishga tushirish (agar rasmda ko'rsatganingizdek kerak bo'lsa)
    Thread(target=run).start()
    
    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi!")
        
