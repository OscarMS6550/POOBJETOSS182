from tkinter import*
from tkinter import Entry
from Codigo import*

ventana = Tk()
ventana.title("GENERADOR DE MATRICULAS")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="White")
seccion1.pack(expand=True,fill='both')

nombre = Label(ventana, text="Ingresa tu nombre:", bg="red")
nombre.place(x=50,y=50)

nombre1 = Entry(width= 30)
nombre1.place(x=200,y=50)

Ap = Label(ventana, text="Ingresa tu Apellido Paterno:", bg="red")
Ap.place(x=50,y=90)

Apaterno = Entry(width= 30)
Apaterno.place(x=200,y=90)

Am = Label(ventana, text="Ingresa tu Apellido Materno:", bg="red")
Am.place(x=50,y=120)

Amaterno = Entry(width= 30)
Amaterno.place(x=200,y=120)


ANacimiento = Label(ventana, text="Año de Nacimiento", bg="red")
ANacimiento.place(x=50,y=150)

aNacimiento = Entry(width=30)
aNacimiento.place(x=200,y=150)

Carrera= Label(ventana, text="Ingresa tu Carrera", bg="red")
Carrera.place(x=50,y=180)

carrera = Entry(width=30)
carrera.place(x=200,y=180)

validaccion = Estudiante(nombre1,Apaterno,Amaterno,ANacimiento,carrera)

BotonValidar=Button(seccion1,text="Validar",bg="#255748",fg="white",command=validaccion.validar)
BotonValidar.pack()



ventana.mainloop()
