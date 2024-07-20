# import crypto
# from rh_project import project as p

# p.run_test_jobs = True
# p.job_repeat_count = 3
# p.schedule_jobs()
# try:
#     while True:
#         p.run()
# except KeyboardInterrupt:
#     print("Exiting...")

# import threading
# import time, os

# def worker_thread():
#     """Vlákno, které běží po ukončení hlavního vlákna."""
#     print("Worker thread spuštěn.")
#     time.sleep(5)  # Simuluje nějakou práci
#     # Otevřete potrubí pro zápis
#     # Otevřete potrubí pro čtení
#     with open('pipe', 'r') as pipe:
#         # Přečtěte data z potrubí
#         line1 = pipe.readline()
#         line2 = pipe.readline()

#         # Vytiskněte data
#         print(line1)
#         print(line2)
#     print("Worker thread ukončen.")


# if __name__ == "__main__":
#     # Vytvořte a spusťte worker thread
#     worker = threading.Thread(target=worker_thread)
#     worker.daemon = False
#     worker.start()

#     with open('pipe', 'w') as pipe:
#         # Odesílejte data do potrubí
#         pipe.write('Ahoj z odesílatele!\n')
#         pipe.write('Další zpráva...\n')

#     # Ukončete hlavní vlákno
#     print("Hlavní vlákno ukončeno.")


# def worker_thread():
#     """Vlákno, které běží po ukončení hlavního vlákna."""
#     print("Worker thread spuštěn.")
#     time.sleep(5)  # Simuluje nějakou práci
#     print("Worker thread ukončen.")


# if __name__ == "__main__":
#     # Vytvořte a spusťte worker thread
#     worker = threading.Thread(target=worker_thread)
#     worker.daemon = False
#     worker.start()

#     # Ukončete hlavní vlákno
#     print("Hlavní vlákno ukončeno.")


# event = threading.Event()  # Sdílená událost

# shared_variable = 0

# def worker_thread():
#     while not event.is_set():  # Kontrola události před každým cyklem
#         print(f"Hodnota sdílené proměnné: {shared_variable}")
#         time.sleep(5)
#     print("Worker thread exiting...")


# if __name__ == "__main__":
#     worker = threading.Thread(target=worker_thread)
#     worker.start()

#     # Měňte sdílenou proměnnou z hlavního vlákna
#     try:
#         while True:
#             shared_variable = int(input("Zadejte novou hodnotu: "))
#     except KeyboardInterrupt:
#         pass

#     # Nastavte událost pro ukončení worker_thread
#     event.set()

#     # Počkejte na ukončení worker_thread
#     worker.join()
