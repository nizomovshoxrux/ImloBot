import logging
from aiogram import Bot, Dispatcher, executor, types
from lotin_krill_lotin import wordTranslator
from checkWord import checkWords

API_TOKEN = '5320120836:AAFhKeEg_tNrSF_YSJ0PltoTzFDirb_iNtI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("uz_imlo Botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring")

@dp.message_handler()
async def checkImlo(message: types.Message):
    words = message.text.split()
    for word in words:
        changeWord = wordTranslator(word) if word.isascii() else word

        result = checkWords(changeWord)

        if result['available']:
            response = f"✅ {wordTranslator(changeWord).capitalize() if word.isascii() else changeWord.capitalize()}"
        else:
            response = f"❌ {wordTranslator(changeWord).capitalize() if word.isascii() else changeWord.capitalize()}\n\n"
            for text in result['matches']:
                response += f"✅ {wordTranslator(text).capitalize() if word.isascii() else text.capitalize()}\n"

        await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)