
class Estudiante():
    def __init__(self,nombre,edad,nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        
    def aprobacion(self):
        if(self.nota >= 60):
            print('DATOS DEL ESTUDIANTE')
            print(f'Nombre: {self.nombre} \nEdad: {self.edad} \nNota: {self.nota} \nAprobado')
        else:
            print('DATOS DEL ESTUDIANTE')
            print(f'Nombre: {self.nombre} \nEdad: {self.edad} \nNota: {self.nota} \nNo Aprobado')
            
alumno1 = Estudiante('Richard',20,75)
alumno1.aprobacion()
