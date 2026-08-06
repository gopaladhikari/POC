from multiprocessing import Process, Value
import time


def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)

    start = time.time()

    process1 = Process(target=increment, args=(counter,))
    process2 = Process(target=increment, args=(counter,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()

    print(f"Total time spent: {end - start:.2f} seconds")

    print(f"Final counter value: {counter.value}")
