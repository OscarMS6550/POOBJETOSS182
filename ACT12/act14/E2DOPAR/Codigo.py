from tkinter import*
import random
from tkinter import messagebox
from datetime import datetime


class Estudiante:
    def __init__(self, nombre1, Apaterno, Amaterno, aNcimiento, carrera,Aactual):
        self.nombre1 = nombre1
        self.Apaterno = Apaterno
        self.Amaterno = Amaterno
        self.aNacimiento = aNcimiento
        self.Actual = Aactual
        self.carrera = carrera
        
    def generar_matricula(self):
       
        anio_actual = datetime.now().year % 100
        if anio_actual < 10:
            anio_actual = '0' + str(anio_actual)
        else:
            anio_actual = str(anio_actual)
      
        anio_nacimiento= self.aNacimiento % 100
        if anio_nacimiento < 10:
            anio_nacimiento = '0' + str(anio_nacimiento)
        else:
            anio_nacimiento = str(anio_nacimiento)
        
        nombre = self.nombre1[0]
        apellido_paterno = self.Apaterno[0]
        apellido_materno  = self.Amaterno[0]
        
        numeros_aleatorios = ''
        for i in range(3):
            numeros_aleatorios += str(random.randint(0, 9))
        abreviatura_carrera = self.carrera[:3].upper()

        return f'{anio_actual}{anio_nacimiento}{nombre}{apellido_paterno}{apellido_materno}{numeros_aleatorios}{abreviatura_carrera}'

        
    
        
               
        
       
       
       
       
     
        
        
        