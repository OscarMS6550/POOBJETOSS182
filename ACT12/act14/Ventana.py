from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import Entry
from codigo import*

ventana = Tk()
ventana.title("Caja Popular Mexicana")
ventana.geometry("600x400")
seccion1=Frame(ventana,bg="White")
seccion1.pack(expand=True,fill='both')

accion = Button(seccion1,text="OPCION SELECCIONADA",bg="#255")
accion.place(x=150,y=200)

met = Label(ventana , text="Opcion Deseada:",bg="black")
met.pack()
opciones = ["Depositar" , "Retirar" , "Consultar Saldo" , "D.Otra Cuenta"]
opcion__seleccionada = tk.StringVar()
Metodo = ttk.Combobox(seccion1,textvariable=opcion__seleccionada,values=opciones)
Metodo.place(x=200,y=250)
ventana.mainloop()



        


    


