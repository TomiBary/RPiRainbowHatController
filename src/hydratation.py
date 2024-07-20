import datetime, csv
import socket

hydration_target = 2.5
current_hydration = 0
start_time = 10  # 10:00
end_time = 22  # 22:00
min_notify_value = 0.5  # when this value is reached, notify user

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def send_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

def check_hydration():
    if current_hydration < hydration_target and start_time <= datetime.datetime.now().hour < end_time:
        ideal_hydration = get_ideal_hydration()
        if ideal_hydration - current_hydration > min_notify_value:
            print(f"Optimalni cil hydratace: {ideal_hydration} \nVypij vodu !!!")
            #TODO run callback function that notifies user that he needs to drink water
        else:
            print(f"Perfektni z aktuálního cíle {ideal_hydration}l je splněno {current_hydration}l")
        #TODO run callback function that updates current_hydration and ideal_hydration

def get_ideal_hydration():
    time = datetime.datetime.now()
    mins_from_start = (time.hour - start_time) * 60 + time.minute  #pocet minut od 10h

    ideal_hydration = hydration_target * mins_from_start / ((end_time - start_time) * 60)  #
    ideal_hydration = max(0, min(ideal_hydration, hydration_target))  # clamp(0, idealni_vypito, hydration_target)
    # print(f"Aktualni optimalni hydratace: {ideal_hydration}")
    return ideal_hydration

#TODO implement method that returns HydratData with ideal_hydration set

#TODO store data somehow in case of restart
# # Uložení dat do CSV souboru
#     with open("hydratace.csv", "a", newline="") as csvfile:
#       writer = csv.writer(csvfile)
#       writer.writerow([cas_nyni.strftime("%Y-%m-%d"), cil_hydratace, vypito])


def add_hydration(amount_litres):
    global current_hydration
    current_hydration += amount_litres