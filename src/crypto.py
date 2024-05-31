import requests

default_symbols = ['BTC', 'ETH', 'KAS']
# url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'  # PROD

parameters = {
    # 'id':'1,1027,20396',
    # 'slug':'bitcoin,ethereum,kaspa',
    'symbol': ",".join(default_symbols),
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '',
}


def fetch_prices(api_key, symbols=None, mock=False):
    params = parameters
    headers['X-CMC_PRO_API_KEY'] = api_key
    if symbols is not None:
        params[
            'symbol'] = symbols  # TODO check if this is correct (if symbols are not list or dict etc.) if it has correct format
    if not mock:
        response = requests.get(url, headers=headers, params=params)

        data = response.json()["data"]

        prices = {}
        for coin in data:
            price = data[coin][0]["quote"]["USD"]["price"]
            prices[coin] = price
    else:
        print("[MOCK] Returning mock prices.....")
        prices = {'BTC': 69404.123456789, 'ETH': 3718.111111111111, 'KAS': 0.130000000000000}
    print(prices)
    return prices
