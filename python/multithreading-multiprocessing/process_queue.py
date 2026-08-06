from multiprocessing import Queue, Process


def prepare_tea(queue: Queue):
    queue.put("hot")


queue = Queue()

if __name__ == "__main__":
    p = Process(target=prepare_tea, args=(queue,))

    p.start()
    p.join()

    print(queue.get())
