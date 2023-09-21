# Ejercicio 6: Implementa un programa Python que solicite al usuario una cadena
# de caracteres (String) y muestre por pantalla dicha cadena, pero con el primer y
# último carácter cambiados de posición.


cadena = input("Ingresa una cadena de caracteres: ")

if len(cadena) >=2:
    cadena_cambiada = cadena[-1]+cadena[1:-1]+cadena[0]
    print(cadena_cambiada)
else:
    cadena_cambiada = cadena[-1]+cadena[0]
    print(cadena_cambiada)