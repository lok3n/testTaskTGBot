import os
from dotenv import load_dotenv
from redis import Redis


class Storage:
    def __init__(self, host, port, password):
        self.r = Redis(host=host, port=port, password=password, ssl=True, decode_responses=True)

    def update_from_dict(self, data):
        for key in data:
            self.r.hmset(key, data[key])

    def get_value(self, currency):
        return float(self.r.hgetall(currency)['Value'].replace(',', '.'))

    def get_name(self, currency):
        return 'Российский рубль' if currency == 'RUB' else self.r.hgetall(currency)['Name']

    def get_rates(self):
        data = {}
        for i in self.r.keys():
            data[i] = self.r.hgetall(i)
        return data


load_dotenv()
storage = Storage(os.getenv('REDIS_HOST'), int(os.getenv('REDIS_PORT')), os.getenv('REDIS_PASS'))
