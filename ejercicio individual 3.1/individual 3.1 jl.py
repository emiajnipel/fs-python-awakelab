# parte 1) Haga una clase llamada Restaurante. El método __init __() para Restaurante debe almacenar dos atributos: un restaurant_nombre y un cocina_tipo.

class Restaurante:
    def __init__(self, nombre, tipo): 
        self.restaurante_nombre = nombre
        self.cocina_tipo = tipo
        self.numero_servicio  = 0  # de la parte N°3

# Cree un método llamado describe_restaurant() que imprima estas dos piezas de información.

    def describe_restaurante(self):
        return "Restaurante {} especializado en: {}.".format(self.restaurante_nombre, self.cocina_tipo)

# y un método llamado abrir_restaurant() que imprima un mensaje indicando que el restaurante está abierto.

    def abrir_restaurante(self):
        return "El restaurante está abierto!!"
 
# de la parte N°3: Agregue un método llamado set_numero_servicio() que le permita establecer el número de clientes que han sido atendidos. Llame a este método con un nuevo número e imprima el valor nuevamente.

    def set_numero_servicio(self, numero):
        self.numero_servicio = numero
        return "Restaurante {}, atendiendo a {} clientes" .format(self.restaurante_nombre, self.numero_servicio)

# de la parte N°3: Agregue un método llamado incrementar_numero_servicio() que le permite incrementar la cantidad de clientes que han recibido servicios. Llame a este método con el número que desee y que pueda representar cuántos clientes se atendieron, digamos, en un día de trabajo.

    def incrementar_numero_servicio(self, incremento):
        self.incremento = incremento
        for i in range(incremento + 1):
            print(" {} atendiendo a {} clientes".format(self.restaurante_nombre, i))
        print()
        return "Todos los clientes fuerón atendidos!."

# Cree una instancia llamada restaurante de la clase. Imprima los dos atributos individualmente y luego llame a ambos métodos.

restaurante = Restaurante("restaurante", "comida")
print(restaurante.restaurante_nombre)
print(restaurante.cocina_tipo)

# Parte 2) Comience con su clase de la Parte 1. Cree tres instancias diferentes de la clase y llame a describe_restaurant() para cada instancia.

juanymedio = Restaurante("Juan y Medio,", "Comida chilena") 
print(juanymedio.describe_restaurante())
subway = Restaurante("SUBWAY", "Sandwich's")
print(subway.describe_restaurante())
terragona = Restaurante("Terragona", "Comida Rapida")
print(terragona.describe_restaurante())

# Parte 3) Comience con su programa de la clase Restaurante. Agregue un atributo llamado numero_servicio con un valor predeterminado de 0. Cree una instancia llamada restaurante de esta clase. Imprima el número de clientes que ha atendido el restaurante y luego cambie este valor e imprímalo nuevamente.

print(restaurante.restaurante_nombre, 'atendio a', restaurante.nmero_servicio, 'clientes')
setattr(restaurante, 'numero_servicio', 3)
print(restaurante.restaurante_nombre, 'atendio a', restaurante.numero_servicio, 'clientes')

# Agregue un método llamado set_numero_servicio() que le permita establecer el número de clientes que han sido atendidos (en la clase, arriba). Llame a este método con un nuevo número e imprima el valor nuevamente.

print(restaurante.set_numero_servicio(25))

# Agregue un método llamado incrementar_numero_servicio() que le permite incrementar la cantidad de clientes que han recibido servicios (en la clase, arriba). Llame a este método con el número que desee y que pueda representar cuántos clientes se atendieron, digamos, en un día de trabajo.

print(restaurante.incrementar_numero_servicio(25))