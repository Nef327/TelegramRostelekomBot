import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6204408225:AAF4Egjy4r7PvwEmG2Qxd6XSQZkcWkE3QPU")
# Диспетчер
dp = Dispatcher()

button_1 = KeyboardButton(text='Дома никого нет')
button_2 = KeyboardButton(text='Есть более приоритетное дело')
button_3 = KeyboardButton(text='Невозможно добраться')
button_4 = KeyboardButton(text='Конец рабочего дня')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=False,
                               keyboard=[[button_1, button_2], [button_3, button_4]])


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Зраствуйте! Вам требуется помощь?", reply_markup=greet_kb)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



# k = "6204408225:AAF4Egjy4r7PvwEmG2Qxd6XSQZkcWkE3QPU"
