# PARTE 1) Usuarios
# Usuarios: cree una clase llamada Usuario. Cree dos atributos llamados nombre y apellido, y luego cree varios otros atributos que normalmente se almacenan en un perfil de usuario.

class Usuario:
    def __init__(self, nombre, apellido, edad, genero, direccion):
        self.nombre_usuario = nombre # requerimiento
        self.apellido_usuario = apellido # requirimiento
        self.edad_usuario = edad # otros atributos
        self.genero_usuario = genero # otros atributos
        self.direccion_usuario = direccion # otros atributos
        self.intentos_de_login = 0 # de la parte 2

# Cree un método llamado "describir_usuario()"" que imprima un resumen de la información del usuario.

    def describir_usuario(self):
        return "usuario nombre: {}, apellido: {}, edad: {} años, género: {}, dirección: {}.".format(self.nombre_usuario, self.apellido_usuario, self.edad_usuario, self.genero_usuario, self.direccion_usuario)

# Cree otro método llamado saludar_usuario() que imprima un saludo personalizado para el usuario.

    def saludar_usuario(self):
        return "Hola {} {}, bienvenido a python".format(self.nombre_usuario, self.apellido_usuario)

# PARTE 2) Intentos de Inicio de Sesión
# Agregue un atributo llamado intentos_de_login a su clase Usuario ya escrita. Escriba un método llamado incrementar_inicios_de_sesion() que incremente el valor de intentos_de_login en 1.

    def incrementar_inicios_de_sesion(self):
        self.intentos_de_login += 1

# PARTE 2) Escriba otro método llamado reset_intentos_de_login que restablezca el valor de intentos_de_login a 0.

    def reset_intentos_de_login(self):
        self.intentos_de_login = 0

# PARTE 1) Cree varias instancias que representen a diferentes usuarios y llame a ambos métodos para cada usuario.

usuario_1 = Usuario("Juan", "Lopez","32", "masculino", "Bilbao #123")
print(usuario_1.saludar_usuario()) # llamando al método saludar_usuario
print(usuario_1.describir_usuario()) # llamando al método describir_usaurio


usuario_2 = Usuario("Juana", "Soto", "28", "femenino", "Alameda #456")
print(usuario_2.saludar_usuario()) # llamando al método saludar_usuario
print(usuario_2.describir_usuario())  # llamando al método describir_usuario

usuario_3 = Usuario("Maria", "Perez", "54", "femenino", "Gran. Avenida #789")
print(usuario_3.saludar_usuario()) # llamando al método saludar_usuario
print(usuario_3.describir_usuario())  # llamando al método describir_usuario

# Cree una instancia de la clase Usuario y llame a incrementar_inicios_de_sesion() varias veces. Imprima el valor de intentos_de_login para asegurarse de que se incrementó correctamente

usuario_1.incrementar_inicios_de_sesion()
usuario_1.incrementar_inicios_de_sesion()
usuario_1.incrementar_inicios_de_sesion()
usuario_1.incrementar_inicios_de_sesion()
usuario_1.incrementar_inicios_de_sesion()
print("Intentos de inicio de sesión:", usuario_1.intentos_de_login)
usuario_1.reset_intentos_de_login()
print("Reiniciando intentos... n° de intentos:", usuario_1.intentos_de_login)