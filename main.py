import aiohttp
import requests
import json


API_URL = 'http://23.111.206.181:8080/register_sale'
API_CSRF = 'http://80.78.246.88/bapi/nft/v1/public/nft/user/csrf-update'

def updateCsrf(headers):
    response = requests.post(API_CSRF,headers)

async def send_buy_request(
        x_checkbot_sitekey,
        x_checkbot_token,
        x_trace_id,
        x_ui_request_trace,
        cookie,
        csrf_token,
        device_info,
        user_agent,
        begin_date
):
    session = aiohttp.client.ClientSession()
    response = await session.post(API_URL,
                                  data=json.dumps({
                                      'x_checkbot_sitekey': x_checkbot_sitekey,
                                      'x_checkbot_token': x_checkbot_token,
                                      'x_trace_id': x_trace_id,
                                      'x_ui_request_trace': x_ui_request_trace,
                                      'cookie': cookie,
                                      'csrf_token': csrf_token,
                                      'user_agent': user_agent,
                                      'device_info': device_info,
                                      'begin_date': begin_date,
                                      **cfg.get_values()
                                  }))
    if response.status != 200:
        raise UserWarning(f'failed to create a buy event: code={response.status}; '
                          f'desc={await response.text()}')

    print('[SUCCESSFUL] Successfully created a buy event')
