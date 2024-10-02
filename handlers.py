from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import F

from utils import get_week_curse, send_curse


def register_handlers(dp, bot):
    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        buttons = [
            [KeyboardButton(text="💰 Получить курс валют 💰")],
            [KeyboardButton(text="📈 Получить динамику за последние 7 дней 📈")],
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True,
        )

        await message.answer(f"Выберите действие!", reply_markup=keyboard)

    @dp.message(F.text == "💰 Получить курс валют 💰")
    async def send_currency_rates(message: Message) -> None:
        await send_curse(bot, message.chat.id)

    @dp.message(F.text == "📈 Получить динамику за последние 7 дней 📈")
    async def choose_currency(message: Message) -> None:
        buttons = [
            [KeyboardButton(text="EUR €")],
            [KeyboardButton(text="USD $")],
            [KeyboardButton(text="Назад")]
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True,
        )

        await message.answer(f"Выберите валюту", reply_markup=keyboard)

    @dp.message(F.text == "EUR €")
    async def get_eur_graph(message: Message) -> None:
        await get_week_curse(bot, 'EUR', message.chat.id)

    @dp.message(F.text == "USD $")
    async def get_usd_graph(message: Message) -> None:
        await get_week_curse(bot, 'USD', message.chat.id)

    @dp.message(F.text == "Назад")
    async def go_back(message: Message) -> None:
        await command_start_handler(message)
