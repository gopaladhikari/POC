from threading import Thread
import time


def prepare_tea(type_, wait_time):
    print(f"Preparing {type_} tea")

    time.sleep(wait_time)

    print(f"{type_} tea prepared")


t1 = Thread(target=prepare_tea, args=("hot", 5))
t2 = Thread(target=prepare_tea, args=("iced", 3))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time spent: {end - start:.2f} seconds")
