from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from dotenv import load_dotenv
from functions.update_currency import update_currency
import asyncio
import os
import logging
from handlers import *

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
dp.include_routers(info_router, course_router, start_router, exchange_router)


async def main():
    await bot.set_my_description(f'ℹ Привет! Я бот для отображения актуального курса валют\n'
                                 f'Мой разработчик @whytek хочет поступить к Вам на работу')
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    scheduler = AsyncIOScheduler()
    await update_currency()
    scheduler.add_job(update_currency, 'cron', hour=6)
    scheduler.start()
    await bot.set_my_commands([BotCommand(command='start', description='Главное меню'),
                               BotCommand(command='rates', description='Актуальные цены'),
                               BotCommand(command='exchange', description='Конвертация')])
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
