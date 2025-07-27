import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputFile

# ✅ التوكن من متغير بيئة لحماية البوت
API_TOKEN = os.getenv("7976144019:AAFA1MNhvg4gL8IQqgxQu8DGViW_ky5QyyY")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("👋 Welcome to AI Resume Pro!\n\nSend me your info (name, job title, experience) and I’ll generate your CV.")

@dp.message_handler()
async def generate_cv(message: types.Message):
    # توليد CV وهمي – في النسخة القادمة بنضيف توليد PDF احترافي
    name = message.text.strip()
    pdf_path = "sample_cv.pdf"
    with open(pdf_path, "wb") as f:
        f.write(b"%PDF-1.4\n% AI Resume Placeholder")
    await message.answer_document(InputFile(pdf_path), caption="Here’s your AI-generated CV 🎯")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
