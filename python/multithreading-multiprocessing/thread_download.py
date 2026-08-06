import threading
import requests
import time


def download(url):
    response = requests.get(url)
    print(f"Downloaded {url}, size: {len(response.content)}")

    return response


urls = [
    "https://images.unsplash.com/photo-1773332598289-ed0444ad1d6f?q=80&w=688&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    "https://images.unsplash.com/photo-1785788684002-f500e756047d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwyfHx8ZW58MHx8fHx8"
    "https://plus.unsplash.com/premium_photo-1785603313094-c633a6be430f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwzfHx8ZW58MHx8fHx8"
]


threads = []


start = time.time()

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()

    threads.append(t)


for t in threads:
    t.join()


end = time.time()

print(f"Total time spent: {end - start:.2f} seconds")
