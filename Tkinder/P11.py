from tkinter import *

#1.- Generar una ventana 
ventana =Tk()
ventana.title("PRACTICA 11")
ventana.geometry("600x400")


#2 Agregar frames 
seccion1=Frame(ventana,bg="green")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="white")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="red")
seccion3.pack(expand=True,fill='both')

#3 
botonAzul= Button(seccion1,text="soy el boton azul ",fg="white")
botonAzul.place(x=60,y=60,width=100,height=35)


botonNegri= Button(seccion2,text="soy el boton Negro ",fg="white",bg="black")
botonNegri.grid(row=0,column=0)

botonAmarillo= Button(seccion2,text="soy el boton amarillo ",fg="black",bg="yellow")
botonAmarillo.grid(row=1,column=1)

botonPurpura= Button(seccion3,text="soy el boton violeta ",fg="white",bg="violet")
botonPurpura.grid(row=5,column=1)



#MOSTRAR LA VENTANA 
ventana.mainloop()







