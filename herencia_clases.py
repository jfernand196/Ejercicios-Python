# Crear una jerarquia de herencia basica

#Persona <- estudiante

class persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

class estudiante(persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera

german = estudiante('123', 'german', 'juan@juan.com', '987', 'sistemas')

print(isinstance(german, estudiante)) ## TRUE
print(isinstance(german, persona)) ## TRUE