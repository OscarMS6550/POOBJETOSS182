from tkinter import*
from tkinter import Entry
from vale import *


ventana = Tk()
ventana.title("APPLE INICIO DE SESION")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="White")
seccion1.pack(expand=True,fill='both')

ic = Label(ventana, text="Ingrese su correo:", bg="red")
ic.place(x=50,y=50)

correoE = Entry(width= 30)
correoE.place(x=200,y=50)

ip = Label(ventana, text="Ingrese su contraseña:", bg="yellow")
ip.place(x=50,y=80)

contraE = Entry(width= 30,show="*")
contraE.place(x=200,y=80)

corr = "oscar123@gmail.com"
contra = "1234"

x=correoE.get()
y=contraE.get()
validacion = Validacion(x, y, corr, contra)

BotonValidar=Button(seccion1,text="Validar",bg="#255748",fg="white",command=validacion.validar)
BotonValidar.pack()
ventana.mainloop()