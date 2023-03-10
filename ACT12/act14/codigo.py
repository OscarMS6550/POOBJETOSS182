from tkinter import*
from tkinter import messagebox

class codigo:
    def __init__ (self,consultar,depositar,ingresar,retirar,numerodecuenta):
        self.__consultar=consultar
        self.__numerodecuenta=numerodecuenta
        self.__depositar=depositar
        self.__ingresar=ingresar
        self.__retirar=retirar
        
    def consultar(self):
        print(f"El saldo actual de la cuenta {self.__numerodecuenta} es de ${self.__consultar}")

            
        