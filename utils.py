from matplotlib import pyplot as plt
from pycbrf import ExchangeRates
import datetime as dt

from aiogram.types import FSInputFile


async def send_curse(bot, chat_id):
    try:
        current_date = str(dt.date.today())
        rates = ExchangeRates(current_date, locale_en=True)
        var_EUR = rates['EUR']
        var_USD = rates['USD']
        text_msg = f"{var_EUR.name} : {var_EUR.value} €\n{var_USD.name} : {var_USD.value} $"
        await bot.send_message(chat_id=chat_id, text=text_msg)
    except Exception as _ex:
        await bot.send_message("Не удалось получить курс валют.")
        print(_ex)


async def get_week_curse(bot, currency, chat_id):
    try:
        today = dt.date.today()
        dates = [str(today - dt.timedelta(days=i)) for i in range(6, -1, -1)]
        values = [ExchangeRates(date, locale_en=True)[currency].value for date in dates]

        plt.title('Динамика за неделю', fontsize=20, fontname='Times New Roman')
        plt.xlabel('Дата (М-Д)', color='gray')
        plt.ylabel(currency, color='gray')
        plt.grid(True)
        plt.plot([date[5:] for date in dates], values, linewidth=2.0)

        file_name = 'currency_dynamics.png'
        plt.savefig(file_name)
        photo = FSInputFile(file_name)
        plt.close()

        await bot.send_photo(chat_id=chat_id, photo=photo)
    except Exception as _ex:
        print("Ошибка в get_week_curse:", _ex)
