import os
import aiohttp
from xml.etree import ElementTree


async def get_currency():
    '''This function get actual currency from site in xml, parse and return dict values'''
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv('CURRENCY_URL')) as resp:
            data = ElementTree.fromstring(await resp.text())
            values = {}
            for d in data:
                values[d[1].text] = {'Name': d[3].text, 'Value': d[4].text}
            return values
