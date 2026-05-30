import threading
import time


def take_order():
    for i in range(1, 4):
        print(f"Order {i} taken")
        time.sleep(1)


def brew_tea():
    for i in range(1, 4):
        print(f"Tea {i} brewed")
        time.sleep(2)


# Create a thread

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_tea)


order_thread.start()
brew_thread.start()


# Wait for the threads to finish or joining the responses

order_thread.join()
brew_thread.join()


print("All tasks completed")
