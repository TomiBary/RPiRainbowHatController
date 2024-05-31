import time
import rainbowhat as rh


def rh_blink_text(text):
    rh_display_text(text)
    time.sleep(1.2)
    rh_display_text()
    time.sleep(0.3)
