import logging

from utils.redis_storage import storage
from functions.get_currency import get_currency


async def update_currency():
    '''Function for updating data from site to redis storage'''
    data = await get_currency()
    storage.update_from_dict(data)
    logging.info('currency updated')

