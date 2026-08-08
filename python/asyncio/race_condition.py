import threading

chai_stock = 0


def get_stock():
    global chai_stock

    for _ in range(10000000):
        chai_stock += 1


threads = [threading.Thread(target=get_stock) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Chai stock: {chai_stock}")
