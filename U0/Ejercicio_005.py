# Ejercicio 5: Implementa un programa Python que solicite al usuario una 
# cadena de caracteres (String) y muestre por pantalla el número de veces que
# aparece la sub-cadena “aaa” dentro de dicho String.

cadena = input("Ingresa una cadena de caracteres: ")
contador = 0

for i in range(len(cadena) - 2):
    if cadena[i:i+3] == "aaa":
        contador += 1

print(f"La subcadena 'aaa' aparece {contador} veces en la cadena proporcionada.")






