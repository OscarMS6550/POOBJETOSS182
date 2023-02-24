from personaje import *
#1SOLICITAR DATOS 

print("")
print("## SOLICITUD DATOS DEL HEROE ##")
especieH = input("Escribe la especie del heroe : ")
nombreH = input("Escribe el nombre del heroe : ")
alturaH = float(input("Altura del Heore : "))
recargaH = int(input("Ingresa las balas del heroe : "))

print("")
print("## SOLICITUD DATOS DEL VILLANO ##")
especieV = input("Escribe la especie del Villano : ")
nombreV = input("Escribe el nombre del Villano : ")
alturaV = float(input("Altura del Villano : "))
recargaV = int(input("Ingresa las balas del villano : "))

#2 CREAMOS LOS 8OBJETOS 
Heroe=personaje(especieH,nombreH,alturaH)
Villano=personaje(especieV,nombreV,alturaV)


Heroe.setNombre("Pepito Calvito")

#ATRIBUTOS HEROE
print("El personaje se llama "+Heroe.getNombre())
print("Pertenece a la especie "+Heroe.getEspecie())
print("y una altura"+str(Heroe.getAltura()))

print("El personaje se llama "+Villano.getNombre())
print("Pertenece a la especie "+Villano.getEspecie())
print("y una altura"+str(Villano.getAltura()))




#Metodos
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargar(recargaH)

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargar(recargaV)
