from aiogram import Bot, Dispatcher, executor, types
from test_dir.file import f
TOKEN = '6328368591:AAH_upq4-VbW9E15cCJ0mpdEi-yVLGH6hHs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=f(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
