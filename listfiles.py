import os
from os import path

from queue import Queue

import time

import threading

def get_folders_files(folder='/'):
    try:
        dirname, folders, files = next(os.walk(folder))
        folders = [path.join(dirname, folder) for folder in folders]
        files = [path.join(dirname, file) for file in files]

        time.sleep(0.1)

        return sorted(folders), sorted(files)
    except:
        return [], []

def naive_print_to_depth(folder='/', max_depth=2):
    if max_depth < 0:
        return 

    folders, files = get_folders_files(folder)

    for file in files:
        print(file)

    for folder in folders:
        naive_print_to_depth(folder, max_depth=max_depth-1)

def multi_threaded_print_to_depth(folder='/', max_depth=2, workers=8):
    queue = Queue()

    def worker():

        try:
            while True:
                folder, depth = queue.get(block=True, timeout=.2)
                folders, files = get_folders_files(folder)

                for file in files:
                    print(file)

                if depth - 1 < 0: continue

                for folder in folders:
                    queue.put((folder, depth - 1))
        except:
            return

    queue.put((folder, max_depth))
    threads = []

    for i in range(workers):
        thread = threading.Thread(target=worker, args=())
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    


    

def timeit(func):
    start = time.time()
    func()
    end = time.time()

    print(f"Took {end - start:0.2f} seconds")

#22.36 seconds
#timeit(naive_print_to_depth)
#3.31 seconds
timeit(multi_threaded_print_to_depth)
