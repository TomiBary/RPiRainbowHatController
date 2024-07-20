import schedule
import threading
import requests
import time, sys, json
from notify_config import CONFIG
import hydratation as h
import utils


class Client:
    def __init__(self):
        self.missing_to_ideal_hydrat = 0

    def run(self): #check_hydrat_local
        schedule.every(CONFIG.check_freq_sec).seconds.do(self.update_missing_hydrat)
        schedule.every(CONFIG.notify_freq_sec).seconds.do(self.show_notification)
        schedule.every(CONFIG.sound_freq_sec).seconds.do(self.play_sound)

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")

    def shouldNotifyUser(self):
        return self.missing_to_ideal_hydrat >= 0.5

    def update_missing_hydrat(self):
        self.missing_to_ideal_hydrat = h.get_ideal_hydration() - h.current_hydration

    def check_and_run(self, callback):
        if self.shouldNotifyUser():
            callback()

    def play_sound(self):
        if not self.shouldNotifyUser():
            return
        def play():
            utils.play_sound("Glass")

        notify_config = CONFIG
        for _ in range(notify_config.get_notify_count()):
            threading.Thread(target=play, daemon=True).start()
        notify_config.notified_without_hydrat += 1

    def show_notification(self):
        if not self.shouldNotifyUser():
            return
        def show():
            utils.display_notification(f"Your water is missing {self.missing_to_ideal_hydrat}L", "Water", "Missing", "Hero")
        threading.Thread(target=show, daemon=True).start()
        # display_notification("You should drink some water!","Hydrat Reminder","subtitle","Pop")

def check_hydrat_network():
    try:
        while True:
            print("Test")
            json = requests.get("http://localhost:8080/hydrat").json()
            if json['current_target'] - json['current'] > 0.5:
                print(f"Napij se !!!")
            time.sleep(3)   # 3 seconds.
    except KeyboardInterrupt:
        pass


# config_keys = ["check_freq_sec", "sound_freq_sec", "notify_freq_sec"]
# if len(sys.argv) >= 2:
#     config_values_from_args = json.loads(sys.argv[1])
#     c = config = {config_keys[i]: config_values_from_args[i] for i in range(len(config_keys))}
#     print(config)
# check_hydrat_local(c['check_freq_sec'], c['sound_freq_sec'], c['notify_freq_sec'])


# ??? =  len(sys.argv) >= 2 and sys.argv[1] in ['T', 't', 'Test', 'test']
cl = Client()
threading.Thread(target=cl.run).start()

try:
    while True:
        print(f'h.current_hydration = {h.current_hydration}, missing_to_ideal_hydrat = {cl.missing_to_ideal_hydrat}')
        amount = float(input("Vypil jsem x litru: "))
        h.add_hydration(amount)
        CONFIG.notified_without_hydrat = 0
except KeyboardInterrupt:
    pass 