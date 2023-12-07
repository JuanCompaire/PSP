#Exercise 3: Cree un hilo que genere números aleatorios entre 1 y 100 y los vaya insertando en una lista,
#y otro que recorra circularmente esa lista y sustituya los números terminados en cero por el valor -1.
#Un tercer hilo abortará los otros dos en el momento en el que la suma de los elementos de la lista supere
#el valor de 20000

import threading
import random

number_list = []

def producer_thread():
    while sum(number_list) <= 20000:
        random_number = random.randint(1, 100)
        number_list.append(random_number)

def modifier_thread():
    while sum(number_list) <= 20000:
        for i in range(len(number_list)):
            if str(number_list[i]).endswith('0'):
                number_list[i] = -1

def main():
    producer = threading.Thread(target=producer_thread)
    modifier = threading.Thread(target=modifier_thread)

    producer.start()
    modifier.start()

    producer.join()
    modifier.join()

    print("Final List:", number_list)

if __name__ == "__main__":
    main()