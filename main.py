import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Указываем токен напрямую
TOKEN = "7592922381:AAHT6g2M8uD3WM2NRet3Gt-fh80Hw7nBv2w"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 Бот Отец")],
        [KeyboardButton(text="🔑 Мой Токен")],
        [KeyboardButton(text="📅 Дата создания бота")],
        [KeyboardButton(text="👤 Мой ВК")],
        [KeyboardButton(text="🚀 Спид тест")]
    ],
    resize_keyboard=True
)

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запустил бота.")
    await message.answer(
        "Приветствую тебя, мой создатель! Я используюсь для тестового запуска и проверки работы бота. "
        "Выбери действие из клавиатуры:",
        reply_markup=menu
    )

# Обработка кнопки "🤖 Бот Отец"
@dp.message(lambda message: message.text == "🤖 Бот Отец")
async def bot_father(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил ссылку на Бота Отца.")
    await message.answer("Ссылка на Бота Отца: https://t.me/BotFather")
    await message.answer("Хотите узнать ещё?", reply_markup=menu)

# Обработка кнопки "🔑 Мой Токен"
@dp.message(lambda message: message.text == "🔑 Мой Токен")
async def my_token(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил токен.")
    await message.answer(f"Ваш токен: {TOKEN}")
    await message.answer("Хотите узнать ещё?", reply_markup=menu)

# Обработка кнопки "📅 Дата создания бота"
@dp.message(lambda message: message.text == "📅 Дата создания бота")
async def creation_date(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил дату создания бота.")
    await message.answer("Дата создания бота: 10 февраля 2025 года.")
    await message.answer("Хотите узнать ещё?", reply_markup=menu)

# Обработка кнопки "👤 Той ВК"
@dp.message(lambda message: message.text == "👤 Той ВК")
async def vk_link(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил ссылку на ВК.")
    await message.answer("Ссылка на ваш ВК: https://vk.com/id107950651")
    await message.answer("Хотите узнать ещё?", reply_markup=menu)

# Обработка кнопки "🚀 Спид тест"
@dp.message(lambda message: message.text == "🚀 Спид тест")
async def speed_test(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил ссылку на Speedtest.")
    await message.answer("Проверьте скорость интернета: https://www.speedtest.net/")
    await message.answer("Хотите узнать ещё?", reply_markup=menu)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")