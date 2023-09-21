# Ejercicio 2: Escribe un programa Python que pregunte al usuario por 10 números 
# enteros y muestre por pantalla el número total de veces que el usuario ha 
# introducido el 0, el número total de enteros mayores que 0 introducidos y
# el número total de enteros menores que 0 introducidos.

igual_a_0 = 0
mayor_a_0 = 0
menor_a_0 = 0

for i in range(0,10):
    i = int(input("Pon un numero entero : "))
    if(i == 0):
        igual_a_0 += 1
    if(i > 0):
        mayor_a_0 += 1
    if(i < 0):
        menor_a_0 += 1

print("Hay "+ str(igual_a_0)+" numero/s  = 0")
print("Hay "+ str(mayor_a_0)+" numero/s > 0")
print("Hay "+ str(menor_a_0)+" numero/s < 0")