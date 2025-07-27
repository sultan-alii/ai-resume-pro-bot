
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputFile

# ✅ التوكن مدمج مباشرة داخل الكود (مؤقتًا للاختبار)
API_TOKEN = "7976144019:AAGT7MnmvHsMgaUvRrdWP9drYjK-gS8bh_c"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("👋 Welcome to AI Resume Pro!

Send me your info (name, job title, experience) and I’ll generate your CV.")

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
