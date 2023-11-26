#Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:
#-El productor produce números enteros mayor que 10 y menor que 1000, el productor produce 10 números
# cada vez que los almacena en la cola y el tiempo de espera entre la generación de un número y
# otro es de PT segundos (1 punto)
#-El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)

#el tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de los siguientes X elementos es de
# CT segundos (1 punto)
#Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
#1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
#4:2 con PT=2  CT=4 y X=2 (0,5 puntos)
#2:10 con PT=1  CT=10 y X=4 (0,5 puntos)
#NOTA DAR UN PEQUEÑO TIEMPO ENTRE EL START DE CADA CONSUMIDOR Y/O PRODUCTOR Y 
# EL SIGUIENTE PARA PODER VER BIEN LOS MENSAJES DEL PRINT

import threading
import queue
import random
import time
from math import gcd

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT

    def run(self):
        while True:
            for _ in range(10):
                numero = random.randint(10, 1000)
                self.queue.put(numero)
                print(numero)
                time.sleep(self.PT)

class Consumer(threading.Thread):
    def __init__(self, queue, CT, X):
        threading.Thread.__init__(self)
        self.queue = queue
        self.CT = CT
        self.X = X

    def run(self):
        while True:
            numeros = []
            for _ in range(self.X):
                numero = self.queue.get()
                print("Los números son: " + str(numero))
                numeros.append(numero)

            mcd = calcular_mcd(*numeros)
            print(f"MCD de {numeros}: {mcd}")
            time.sleep(self.CT)

def calcular_mcd(*numeros):
    return gcd(*numeros)

# Caso 1:1 con PT=1, CT=4 y X=3
q_1_1 = queue.Queue()
p_1_1 = Productor(q_1_1, PT=1)
c_1_1 = Consumer(q_1_1, CT=4, X=3)

# Caso 4:2 con PT=2, CT=4 y X=2
q_4_2 = queue.Queue()
p_4_2 = Productor(q_4_2, PT=2)
c_4_2 = Consumer(q_4_2, CT=4, X=2)

# Caso 2:10 con PT=1, CT=10 y X=4
q_2_10 = queue.Queue()
p_2_10 = Productor(q_2_10, PT=1)
c_2_10 = Consumer(q_2_10, CT=10, X=4)

# Iniciar los hilos
p_1_1.start()
time.sleep(1)
c_1_1.start()

p_4_2.start()
time.sleep(1)
c_4_2.start()

p_2_10.start()
time.sleep(1)
c_2_10.start()

# Esperar a que los hilos terminen
p_1_1.join()
c_1_1.join()

p_4_2.join()
c_4_2.join()

p_2_10.join()
c_2_10.join()