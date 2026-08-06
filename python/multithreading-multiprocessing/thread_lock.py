import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter

    for _ in range(100_000):
        with lock:
            counter += 1

    print(counter)


def decrement():
    global counter

    for _ in range(100):
        with lock:
            counter -= 1

    print(counter)


increment_threads = [threading.Thread(target=increment) for _ in range(20)]

decrement_threads = [threading.Thread(target=decrement) for _ in range(20)]

for thread in increment_threads:
    thread.start()


for thread in increment_threads:
    thread.join()

print(f"Final counter value:{counter}")
