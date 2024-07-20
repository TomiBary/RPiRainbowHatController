from rh_utils import get_crypto_price_message, rh_display_text
from datetime import datetime as dt
import time
import rh_project as p


def fetch_crypto_prices_job(*args):
    msg = get_crypto_price_message()
    msg.text *= args[0]
    p.project.message = msg
    print(f"Fetched crypto prices")
    return True


def display_crypto_prices_job(*args):
    msg = args[0] if args and args[0] else p.project.message
    print("Crypto prices:" + msg.text)
    while msg.is_next():
        time.sleep(0.15)
        text = msg.get_next()
        rh_display_text(text)
    rh_display_text()
    msg.set_index(0)
    return True


def display_time_job(*args):
    current_time = dt.now().strftime('%H.%M')
    print("Time:" + current_time)
    blink_text(current_time)
    return True


def display_date_job(*args):
    current_date = dt.now().strftime('%d.%m.')
    print("Date:" + current_date)
    blink_text(current_date)
    return True


def blink_text(text):
    rh_display_text(text)
    time.sleep(1.5)
    rh_display_text()
    time.sleep(0.5)
