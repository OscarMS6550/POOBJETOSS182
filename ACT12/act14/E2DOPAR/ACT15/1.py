from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana = Tk()
Ventana.title("INICIO DE USUARIOS")
Ventana.geometry("500x300")
panel = ttk.Notebook(Ventana)
panel.pack(fill='both',expand='yes')
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

#PESTAÑA 1:FORMULARIO 
titulo = Label(pestana1,text="Registrar el Usuario",fg="blue",font=("Modern",18)).pack()
varNom= tk.StringVar()
LblNom=Label(pestana1,text="Nombre:").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

#PESTAÑA 2:Correo
varCor= tk.StringVar()
LblCor=Label(pestana1,text="Correo:").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
LblCon=Label(pestana1,text="Contrasena:").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()

btnGuardar=Button(pestana1,text="Guardar Datos").pack()






panel.add(pestana1,text="Ingrese los datos : ")
panel.add(pestana2,text="Buscar Usuario : ")
panel.add(pestana3,text="Consultar usuario: ")
panel.add(pestana4,text="Actualizar Usuario : ")


Ventana.mainloop()



