# Ejercicio 10: Implementa un método Python llamado mayorYmenor,
# el cual recibe como parámetro una tabla de Strings y muestra por pantalla el
# String con mayor longitud y el String con menor longitud.

tabla = ["comida","perro","lagarto","Daniel","salamadandra","pez"]

def mayorYmenor(tabla):
    max = tabla[0]
    for i in range(len(tabla)):
        if(len(max)<len(tabla[i])):
            max = tabla[i]
    print("La palabra más larga es "+max)
    min = tabla[0]
    for z in range(len(tabla)):
        if(len(min)>len(tabla[z])):
            min = tabla[z]
    print("La palabra más corta es "+min)

mayorYmenor(tabla)






