import asyncio
import os
from dotenv import load_dotenv
from os.path import join, dirname

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import register_handlers


async def main() -> None:
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Регистрируем хэндлеры
    register_handlers(dp, bot)

    # Стартуем поллинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())