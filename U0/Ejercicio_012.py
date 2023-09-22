#Ejercicio 12:Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
# Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
# - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa,
# no se hará nada.
# - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que
# nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.


class Cuenta:
    def __init__(self,titular,cantidad = 0.0):
        self.titular = titular
        if(cantidad >0):
            self.cantidad = cantidad
        else:
            self.cantidad = 0.0

    def ingresar(self,cantidad):
        if cantidad>0:
            self.cantidad +=cantidad

    def retirar(self,cantidad):
        if cantidad>0:
            if self.cantidad-cantidad >0:
                self.cantidad -=cantidad
            else:
                self.cantidad = 0.0

    def __str__(self):
        return f'Cuenta [titular={self.titular}, cantidad={self.cantidad}]'

cuenta1 = Cuenta("juan",160)
print("La cuenta de "+cuenta1.titular+" tiene un balance de : "+str(cuenta1.cantidad)+" €")

cuenta1.ingresar(16)
print("La cuenta de "+cuenta1.titular+" tiene un balance de : "+str(cuenta1.cantidad)+" €")

cuenta1.retirar(100)
print("La cuenta de "+cuenta1.titular+" tiene un balance de : "+str(cuenta1.cantidad)+" €")


