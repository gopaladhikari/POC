import threading
import time


def monitor_tea_temp():
    while True:
        print("Checking tea temperature...")
        time.sleep(1)


thread = threading.Thread(target=monitor_tea_temp)
thread.start()


print("Main program is done...")
