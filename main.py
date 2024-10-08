import time
import requests
import json
import threading
# import concurrent.futures

lock = threading.Lock()

def init_file():
    with open("data.json", "w") as start_file:
        json.dump([], start_file )


def fetch_data(idx):
    url = f"https://jsonplaceholder.typicode.com/posts/{idx}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with lock:
            with open("data.json", "r") as outfile:
                data_list = json.load(outfile)
                # print(data_list)
            data_list.append(data)
            with open("data.json", "w") as outfile:
                json.dump(data_list, outfile, indent=2)
    else:
        print(f"Error: {response.status_code}")


if __name__ == '__main__':
    start = time.perf_counter()
    print(f"start time {start}")
    init_file()

    threads = []
    # threading ბიბლიოთეკით
    for i in range(1,78):
        thread = threading.Thread(target=fetch_data, args=(i,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


    # concurrent.futures ბიბლიოთეკით
    # with concurrent.futures.ThreadPoolExecutor(max_workers=77) as executor:
    #     for i in range(1,78):
    #         thread = executor.submit(fetch_data, i)
    #         # threads.append(thread)


    end = time.perf_counter()
    print(f"end time {round(end - start, 2)}")

