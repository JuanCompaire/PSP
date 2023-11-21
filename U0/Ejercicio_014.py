#Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
# - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
# - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
# - 3. Salir del Programa

import os

opciones = [1,2,3]
inicio = None
text = []
texto = " "

while(inicio not in  opciones):
    inicio = int(input("Elige una opcion : 1-Escritura, 2-Lectura, 3-Salir --> : "))

    if inicio == 1:
        for i in range(1,101):
            if i%2 == 0:
                text.insert(i,i)
    texto = " ".join(map(str, text))
    with open("pares_100.txt","w") as file:
        file.write(texto)

    if inicio == 2:
        try:
            with open("pares_100.txt", "r") as file:
                contenido = file.read()
            print("Contenido de 'pares_100.txt':")
            print(contenido)
        except FileNotFoundError:
            print("El archivo 'pares_100.txt' no existe.")

    if inicio == 3: 
        print("Saliste")
        break
        
