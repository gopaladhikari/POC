from multiprocessing import Process
import time


def brew_tea(name: str):
    for i in range(1, 4):
        print(f"{name} brewing tea {i}")
        time.sleep(2)


if __name__ == "__main__":
    tea_makers = [
        Process(target=brew_tea, args=(f"Tea maker {i }",)) for i in range(1, 4)
    ]

    # Start all process

    for tea_maker in tea_makers:
        tea_maker.start()

    # Wait for all processes to finish
    for tea_maker in tea_makers:
        tea_maker.join()

print("All tasks completed")
