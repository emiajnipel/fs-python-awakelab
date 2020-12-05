import random

# Individual, desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. y un método para imprimir los datos en la clase Cuenta.

class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.cantidad = random.randint(1000000, 10000000)

    def imprimir_datos(self):
        return f'Titular de cuenta: {self.titular}, \nSaldo disponible: ${self.cantidad}'

# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
class Caja_ahorro(Cuenta):
    def __init__(self, titular):
        Cuenta.__init__(self, titular)

    def imprimir_datos(self):
        return f'Titular de cuenta: {self.titular}, \nAhorros disponibles:$ {self.cantidad}'

# La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
class Plazo_fijo(Cuenta):
    def __init__(self, titular):
        Cuenta.__init__(self, titular)
        self.plazo = random.randint(12, 36) 
        self.interes = 0

    #Tendrá un método para obtener el importe del interés (cantidad*interés/100)
    def importe_interes(self, interes):
        self.interes = interes
        self.importe_mensual = (self.cantidad * self.interes) / 100
        self.importe_total = self.importe_mensual * self.plazo

    # otro método para mostrar la información, datos del titular plazo, interés y total de interés.
    def imprimir_datos(self):
        return f'Titular de cuenta: {self.titular} \nSaldo disponible $ {self.cantidad} \nPlazo: {self.plazo} meses \nInterés: {self.interes} % \nImporte mensual $ {round(self.importe_mensual)} \nImporte total $ {round(self.importe_total)}'


# Crear al menos un objeto de cada subclase.
# Muestre el uso práctico de atributos y métodos de distintos objetos de cuenta, unos de plazo fijo y otros de caja ahorro.

print() 
cuenta_uno = Cuenta('Andrés Tresado')
print(cuenta_uno.imprimir_datos())
print()
cuenta_dos = Caja_ahorro('Joaquín Odoro')
print(cuenta_dos.imprimir_datos())
print()
deposito = Plazo_fijo('Mario Neta')
deposito.importe_interes(float(input('Ingresa el porcentaje de interés:\n'))) # ingresando tasa de interés.
print(deposito.imprimir_datos())
# sumando interés de deposito a cantidad inicial.
print('Al finalizar tú desposito acumularas:$', (int(deposito.importe_total + deposito.cantidad)))