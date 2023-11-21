#Ejercicio 15: Crea un fichero de texto con el nombre y contenido que tú desees.
# Por ejemplo, Ejercicio15.txt. Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y
# muestre su contenido por pantalla sin espacios. Por ejemplo,
# si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”.

with open("Ejercicio15.txt","w") as file:
    file.write("Hola Gorka, esto es un ejercicio para usted")
    
try:
 with open("Ejercicio15.txt","r") as file:
        texto = file.read()
        texto_cambiar = ""
        
        for i in range (len(texto)):
            if texto[i] != " ":
                texto_cambiar += texto[i]        
        print(texto_cambiar)

except FileNotFoundError:
    print("no se ha encontrado el archivo")
    