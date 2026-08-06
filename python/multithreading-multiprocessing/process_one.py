# import threading
import time
from multiprocessing import Process


def cpu_heavy():
    print("Crunching numbers...")

    total = 0

    for _ in range(10**8):
        total += 1

    print("Total:", total)


if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end = time.time()

    print(f"Total time spent: {end - start:.2f} seconds")
