import datetime
import json
import os
import socket
from hydrat_data import HydratData, Config

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FILE_PATH = "resources/hydrat.csv"
config = Config()  # Load static config


def get_ideal_hydration():
    time = datetime.datetime.now()
    mins_from_start = (time.hour - config.start_time) * 60 + time.minute  # pocet minut od 10h

    ideal_hydration = config.daily_target * mins_from_start / ((config.end_time - config.start_time) * 60)  #
    ideal_hydration = max(0, min(ideal_hydration, config.daily_target))  # clamp(0, idealni_vypito, hydration_target)
    # print(f"Aktualni optimalni hydratace: {ideal_hydration}")
    return ideal_hydration


# TODO create method that loads HydratData sort them by date and store them again
def load_all_from_csv():
    if not os.path.exists(FILE_PATH):
        print(f"File {FILE_PATH} does not exist.")
        return
    with open(FILE_PATH, "r") as csvfile:
        return csvfile.readlines()


def save_to_csv(data: HydratData):
    all_rows = load_all_from_csv()
    today_hydrat_data = try_get_today_hydrat_data(all_rows)
    if today_hydrat_data:
        all_rows[-1] = data.to_json(as_list=True) + "\n"
        with open(FILE_PATH, "w") as csvfile:
            csvfile.writelines(all_rows)
            return True

    with open(FILE_PATH, "a") as csvfile:
        csvfile.write(data.to_json(as_list=True) + "\n")
        return True


# def check_hydration():
#     if hydrat.current < config.daily_target and config.start_time <= datetime.datetime.now().hour < config.end_time:
#         ideal_hydration = get_ideal_hydration()
#         if ideal_hydration - hydrat.current > config.min_notify_value:
#             print(f"Optimalni cil hydratace: {ideal_hydration} \nVypij vodu !!!")
#             # TODO run callback function that notifies user that he needs to drink water
#         else:
#             print(f"Perfektni z aktuálního cíle {ideal_hydration}l je splněno {hydrat.current}l")
#         # TODO run callback function that updates current_hydration and ideal_hydration

def is_today(date):
    return date.date() == datetime.datetime.now().date()


def parse_date_time(date_time_str):
    return datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')


def try_get_today_hydrat_data(all_data):
    try:
        row = json.loads(all_data[-1])
        if is_today(parse_date_time(row[0])):
            return HydratData(get_ideal_hydration(), row[1], row[2])
    except Exception as e:
        print(f"Failed to parse date_time from last row: {e}")
        return None


def get_hydrat_data():
    today_hydrat_data = try_get_today_hydrat_data(load_all_from_csv())
    if today_hydrat_data is not None:
        return today_hydrat_data
    return HydratData(get_ideal_hydration(), current=0)


def send_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")


# print(get_hydrat_data())
# save_to_csv(HydratData(2.0045645, 1.555555))
