import asyncio
import time
import json
import aiohttp
import main

from json import dumps
from config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver

results = []

def getAuctionPage():
    time.sleep(3)
    url = f'https://www.binance.com/ru/nft/goods/blindBox/detail?productId={product_id}&isOpen=true&isProduct=1'
    driver.get(url)
    time.sleep(3)
    driver.find_elements(By.XPATH, "//button")[1].click()
    main.updateCsrf(json.dumps(driver.get_cookies()))
    time.sleep(2)


def clickConfirm():
    search = driver.find_elements(By.XPATH,'//button')[-1]
    ActionChains(driver).move_to_element(search).click().perform()
    time.sleep(2.5)

    for request in driver.requests:

        if str(request.url) == 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create':
            cookies = request.headers['cookie']
            csrftoken = request.headers['csrftoken']
            deviceinfo = 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg1OCwxNTI1IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODEzLDE1MjUiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgNyIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZW4tVVMiLCJ0aW1lem9uZSI6IkdNVCs2IiwidGltZXpvbmVPZmZzZXQiOi0zNjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImxpc3RfcGx1Z2luIjoiIiwiY2FudmFzX2NvZGUiOiIyOWI5YmU4MyIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwoUikgSEQgR3JhcGhpY3MgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wKSIsImF1ZGlvIjoiMzUuNzM4MzI5NTkzMDkyMiIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL0FsbWF0eSIsImRldmljZV9uYW1lIjoiRmlyZWZveCBWOTMuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6Ijg3YmY0OTA2ZDU3NDc4ZTE0NjAwMzQwYmY3MWUyYTUzIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTYyOTEzODQ2NTA4NHBCVTJIS2JOeWhjRWRKRkpHMGksMTYyOTk4Mjk5NzgwMnBPQWVDMGRmcldqUUZxV2NZTmEsMTYyOTk4NTIzMTY3MXlndGlyOFhBOWZWWW93TWFRRDcifQ=='
            useragent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'

            xNftCheckbotSitekey = request.headers['x-nft-checkbot-sitekey']
            xNftCheckbotToken = request.headers['x-nft-checkbot-token']
            xTraceId = request.headers['x-trace-id']
            xUiRequestTrace = request.headers['x-ui-request-trace']

            return {
                'Host': 'www.binance.com',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'clienttype': 'web',
                'x-nft-checkbot-token': xNftCheckbotToken,
                'x-nft-checkbot-sitekey': xNftCheckbotSitekey,
                'x-trace-id': xTraceId,
                'x-ui-request-trace': xUiRequestTrace,
                'content-type': 'application/json',
                'cookie': cookies,
                'csrftoken': csrftoken,
                'device-info': deviceinfo,
                'user-agent': useragent
            }

    return {}


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.binance.com/ru/nft/market")
a = input('?????????????????????? ?? ?????????????? Enter: ')

getAuctionPage()

def get_tasks(session):
    url = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'
    tasks = []

    for i in range(0, requests_count):
        tasks.append(asyncio.create_task(session.post(url, data=json.dumps(requests_payload), ssl=False)))

    print(len(tasks))
    return tasks


async def get_symbols(headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = get_tasks(session)
        print(time.time())
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())


def startSsc(headers):
    try:
        return asyncio.get_event_loop().run_until_complete(get_symbols(headers))
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop().run_until_complete(get_symbols(headers))

def sendToServ(headers):
    if not headers:
        print('ERROR: no headers')
        raise SystemExit(1)
    try:
        asyncio.run(main.send_buy_request(
            headers['x-nft-checkbot-token'],
            headers['x-nft-checkbot-sitekey'],
            headers['x-trace-id'],
            headers['x-ui-request-trace'],
            headers['cookie'],
            headers['csrftoken'],
            headers['device-info'],
            headers['user-agent'],
            time.time() + 5
        ))
    except:
        print('Failed to send info')

while True:
    ts = time.time()
    if sale_time>ts:
        print(f'{sale_time-ts} - ???????????????? ????????????')
    if sale_time-ts < 13.0:
        break

headers = clickConfirm()

while True:
    ts = time.time()
    if sale_time>ts:
        print(f'{sale_time-ts} - ???????????????? ????????????')
    if sale_time<ts:
        startSsc(headers)
        break


for r in results:
    if len(r)>250:
        print('blocked')
    else:
        print(r)

q = input()