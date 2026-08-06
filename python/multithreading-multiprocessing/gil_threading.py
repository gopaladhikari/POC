# Global Interpreter Lock in Threading


import threading
import time


def brew_tea():
    print(f"{threading.current_thread().name} started brewing tea")
    count = 0

    for _ in range(100_000_000):
        count += 1

    print(f"{threading.current_thread().name} finished brewing tea")
    return count


thread1 = threading.Thread(target=brew_tea, name="Waiter 1")
thread2 = threading.Thread(target=brew_tea, name="Waiter 2")


# Start the threads

start = time.time()

thread1.start()
thread2.start()


# Wait for the threads to finish and join them

thread1.join()
thread2.join()


end = time.time()

print(f"Total time spent: {end - start:.2f} seconds")
