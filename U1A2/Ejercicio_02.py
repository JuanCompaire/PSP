import multiprocessing as mp
import os

def print_cube(num):
    print("The cube of {} is {}".format(num, num * num * num))

def print_square(num):
    print("The square of {} is {}".format(num, num * num))

if __name__ == '__main__':
    
    pool = mp.Pool(processes = 2)

    numbers = [1,2,3]

    pool.starmap(print_cube, [(num,) for num in numbers])
    pool.starmap(print_square, [(num,) for num in numbers])

    pool.close()
    pool.join()