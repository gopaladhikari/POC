# Global Interpreter Lock in Multiprocessing


from multiprocessing import Process
import time


def crunch_number():
    print(f"Started the count process")
    count = 0

    for _ in range(100_000_000):
        count += 1

    print(f"Finished the count process")
    return count


if __name__ == "__main__":
    start = time.time()

    process1 = Process(target=crunch_number)
    process2 = Process(target=crunch_number)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()

    print(f"Total time spent: {end - start:.2f} seconds")
