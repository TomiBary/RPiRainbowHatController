import socket
from sys import argv
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

opened_sockets = []

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode('utf-8'))

def receive_data(callback=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if data == 'q':
                    break
                if not data:
                    continue
                print(f'Received: {data.decode('utf-8')}')
                if callback:
                    callback(data)


if len(argv) < 2 or argv[1] not in ['R', 'r', 'S', 's']:
    print(f'Wrong or not enough arguments ({len(argv)}). Use R or S.')
else:
    try:
        if argv[1] in ['R', 'r']:
            receive_data()
        if argv[1] in ['S', 's'] and len(argv) >= 3:
            send_data(argv[2])
    except KeyboardInterrupt:
        pass
