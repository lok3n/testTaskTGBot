from functions.exchange import exchange
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.redis_storage import storage

exchange_router = Router()


@exchange_router.message(Command('exchange'))
async def exchange_command_handler(message: Message):
    data = message.text.split()
    if len(data) != 4 or len(data[1]) != 3 or not data[1].isalpha() or len(data[2]) != 3 or not data[2].isalpha() or not \
            data[3].isdigit():
        return await message.answer(
            '❌ Ошибка! Формат использования комманды:\n/exchange [из какой валюты] [в какую валюту] [сумма]\n\n'
            '👉 Пример использования, который покажет сумму 10 долларов в рублях\n/exchange USD RUB 10')
    command, from_currency, to_currency, amount = data
    result = await exchange(from_currency, to_currency, int(amount))
    await message.answer(f'🔎 Результат конвертации из <i>{storage.get_name(from_currency)}</i> в '
                         f'<i>{storage.get_name(to_currency)}</i>: <b>{result}</b>', parse_mode='HTML')
