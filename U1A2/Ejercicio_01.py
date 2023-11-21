import multiprocessing as mp
import os

def my_id(task_id):
    process_id = os.getpid()
    print(f"Hi, I'm worker {task_id} (with PID {process_id})")

    



if __name__ == '__main__':
    num_cores = mp.cpu_count()-1;

    pool = mp.Pool(processes =num_cores)

    tasks = num_cores*2

    pool.map(my_id, range(tasks))

    pool.close()
    pool.join()