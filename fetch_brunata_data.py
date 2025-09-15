import aiohttp
import asyncio
import configparser
import json

import libs.brunata.api as brunata_api

async def main():
    # load credentials from config file
    config = configparser.ConfigParser()
    config.read('brunata-secrets.cfg')
    username = config.get('brunata', 'username')
    password = config.get('brunata', 'password')

    # initialize Brunata API client
    session = aiohttp.ClientSession()
    brunata_client = brunata_api.BrunataOnlineApiClient(username, password, session)

    # try to fetch all available data
    await brunata_client.fetch_meters()
    await brunata_client.fetch_consumption(brunata_api.Consumption.WATER, brunata_api.Interval.MONTH)
    await brunata_client.fetch_consumption(brunata_api.Consumption.ELECTRICITY, brunata_api.Interval.MONTH)
    await brunata_client.fetch_consumption(brunata_api.Consumption.HEATING, brunata_api.Interval.MONTH)
    json_data = brunata_client.get_consumption()

    # format and print the fetched data
    print(json.dumps(json_data, indent=4))

    await session.close()

asyncio.run(main())
