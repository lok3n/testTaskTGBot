from utils.redis_storage import storage


async def exchange(from_currency, to_currency, amount):
    '''Function to converting currencies from one to another'''
    if to_currency != 'RUB':
        amount = amount / storage.get_value(to_currency)
    amount = round(amount * storage.get_value(from_currency), 4)
    return amount
