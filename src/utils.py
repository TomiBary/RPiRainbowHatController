from math import log10, floor
import crypto
from scroll_msg import ScrollMessage
import yaml

import rainbowhat as rh

display_digits = 4
space = ' '


def format_price(price: float):
    # Define the suffixes for different magnitudes
    suffixes = ['', 'K', 'M', 'G', 'T', 'P']

    # Find the index of the suffix to use
    magnitude = max(0, min(len(suffixes) - 1, int(floor(log10(price) / 3))))

    switcher = {
        0: 4,
        1: 4,
        2: 3,
        3: 2,
        4: 1,
    }
    whole_part = len(str(price).split('.')[0])
    return f"{price / 10 ** (3 * magnitude):.{switcher.get(whole_part, 0)}f}{suffixes[magnitude]}"
    # return '{:.{prec}f}'.format(price, prec=switcher.get(whole_part, 0))


def format_to_price_list(prices):
    return [f"{format_price(price)} {coin}" for coin, price in prices.items()]


def get_display_text(prices):
    formatted_prices = format_to_price_list(prices)
    formatted_prices.append('-')
    spaces4 = space * 2
    return spaces4 + spaces4.join(formatted_prices)


def get_crypto_price_message():
    with open('private.yml', 'r') as f:
        api_key = yaml.safe_load(f)['API_KEY_PROD']

    prices = crypto.fetch_prices(api_key)
    txt = get_display_text(prices)
    return ScrollMessage(txt)


def rh_display_text(text="    "):
    rh.display.print_number_str(text)
    rh.display.show()
    # pass
