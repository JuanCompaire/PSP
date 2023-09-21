# Ejercicio 3: ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que
# adivine el número. El programa generará un número aleatorio entre 0 y 20 y
# luego irá pidiendo números al usuario indicando “mayor” o “menor” según sea mayor o
# menor con respecto al número generado aleatoriamente.
# El proceso termina cuando el usuario acierta, y
# deberá mostrar un mensaje de felicitaciones junto al número de intentos que
# ha necesitado el usuario.

import random

numero_acertar = random.randint(0,20)
intentos = 1

numero = int(input("Adivina el numerin : "))

while numero != numero_acertar:
    if(numero > numero_acertar):
        numero = int(input("Es un numero MÁS PEQUEÑO, prueba otra vez : "))
        intentos += 1
    else:
        numero = int(input("Es un numero MÁS GRANDE, prueba otra vez : "))
        intentos += 1


print("¡¡¡Has acertado el numero, en "+str(intentos)+ " intentos!!!")
