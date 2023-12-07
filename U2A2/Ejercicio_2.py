#Exercise 2: Using the multithreading module, write a python program as follows:
#● Create a pool of threads to run concurrent tasks.
#● The pool size should be 3.
#● Create and fill an array of 100 random integer numbers.
#● Run all 3 threads to parse the vector data. One of them must show the mean, another
#the maximum and minimum value, and the last one the standard deviation. Note that
#although these processes share the vector, they only do so for reading. None of them
#must modify any value of the vector.

import threading
import random
import numpy as np

vector_data = np.random.randint(1, 100, 100)

def mean_thread():
    mean = np.mean(vector_data)
    print(f"Mean: {mean}")

def min_max_thread():
    minimum = np.min(vector_data)
    maximum = np.max(vector_data)
    print(f"Min: {minimum}, Max: {maximum}")

def std_deviation_thread():
    std_dev = np.std(vector_data)
    print(f"Standard Deviation: {std_dev}")

def main():
    pool_size = 3
    threads = []

    threads.append(threading.Thread(target=mean_thread))
    threads.append(threading.Thread(target=min_max_thread))
    threads.append(threading.Thread(target=std_deviation_thread))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()