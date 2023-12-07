#Exercise 4: Cree un programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y
#el 1000. Muestre el resultado de cada hilo. Ganará el hilo que consiga el número mas alto.

import threading
import random

results = []

def sum_thread(thread_id):
    random_numbers = [random.randint(1, 1000) for _ in range(100)]
    thread_sum = sum(random_numbers)
    results.append((thread_id, thread_sum))
    print(f"Thread {thread_id}: Sum = {thread_sum}")

def main():
    threads = []
    
    for i in range(1, 11):
        thread = threading.Thread(target=sum_thread, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    winner = max(results, key=lambda x: x[1])
    print(f"\nWinner: Thread {winner[0]} with sum {winner[1]}")

if __name__ == "__main__":
    main()