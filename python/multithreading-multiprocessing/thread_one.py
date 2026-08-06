from threading import Thread
import time


def boil_milk():
    print("Boiling milk")
    time.sleep(5)
    print("Milk boiled")


def toast_bun():
    print("Toasting bun")
    time.sleep(3)
    print("Bun toasted")


start = time.time()

t1 = Thread(target=boil_milk)
t2 = Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time spent: {end - start:.2f} seconds")
