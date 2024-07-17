import requests

import threading
import time, os

print('playing sound using native player')
os.system("afplay /System/Library/Sounds/Ping.aiff")

def check_hydrat():
    while True:
        print("Test")
        json = requests.get("http://localhost:8080/hydrat").json()
        if json['current_target'] - json['current'] > 0.5:
            print("Napij se !!! {}".format(os.getpid()))
        time.sleep(3)   # 3 seconds.

# Start execution in the background.
# t = threading.Thread(target=check_hydrat)
# print(t.get_native_id())
# t.start()