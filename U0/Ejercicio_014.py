# Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
#- 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
#- 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
#- 3. Salir del Programa.

def escribir():
    with open("pares.txt","w") as file:
        for i in range(0,101,2):
            file.write(str(i)+", ")
        
    print("escritura realizada")

def leer():
    try:
        with open("pares.txt", "r") as file:
            lectura = file.read()
            print("Contenido del archivo 'numeros_pares.txt':")
            print(lectura)
    except FileNotFoundError:
        print("El archivo 'numeros_pares.txt' no existe.")
    
while True:
    opcion = input("Seleccione una opción 1.Escritura, 2.Lectura, 3.Salir, selecciona tu opción : ")
    
    if opcion == "1":
        escribir()
    elif opcion == "2":
        leer()
    elif opcion == "3":
        print("Exit.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")
