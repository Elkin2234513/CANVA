from tkinter import *
import random
#variable globales
BASE = 460
ALTURA = 220

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("ELKIN REX")
# tamaño de la ventana
ventana_principal.geometry("500x500")
# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="black")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=240)
frame_graficacion.place(x=10, y=10)
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="green", width=480, height=250)
frame_grafica.place(x=10, y=10)

#creacion canva
c = Canvas(frame_graficacion ,width=BASE, height= ALTURA)
c.place(x=10 , y=10)
c.config(bg="yellow")

#lineas
#Linea1 = c.create_line(10,10, BASE-10,10, fill = "red")
#Linea2 = c.create_line(BASE-10,10, BASE-10,ALTURA-10, fill = "red")
#Linea3 = c.create_line(BASE-10,ALTURA-10, 10,ALTURA-10, fill = "red")
#Linea4 = c.create_line(10,ALTURA-10, 10,10,  fill = "red")

#linea5=c.create_line(BASE-10,10, 10,ALTURA-10, fill="Blue") #DIAGONAL

#ARCO
#arc1 =c.create_arc((BASE/2)-30,(ALTURA/2)-30,(BASE/2)+30,(ALTURA/2)+30, start=45,extent=45, fill="black")

#linea7 = c.create_line(BASE/2 - 20,ALTURA/2 -60,BASE/2 + 20,ALTURA/2 -60, fill="red")
#linea8 = c.create_line(BASE/2 + 20,ALTURA/2 -60,BASE/2 + 20,ALTURA/2 -20, fill="red")
#linea9 = c.create_line(BASE/2 + 20,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 -20, fill="red")
#linea10 = c.create_line(BASE/2 + 60,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 +20, fill="red")
#linea11 = c.create_line(BASE/2 + 60,ALTURA/2 +20,BASE/2 + 20,ALTURA/2 +20, fill="Blue")
#linea12 = c.create_line(BASE/2 + 20,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 -20, fill="red")
#linea13 = c.create_line(BASE/2 + 60,260+BASE/2, fill="Blue")
#linea14 = c.create_line(220,100,260,100, fill="red")
#linea15 = c.create_line(220,100,260,100, fill="red")
#linea16 = c.create_line(220,100,260,100, fill="red")
#linea17 = c.create_line(220,100,260,100, fill="red")
#linea18 = c.create_line(220,100,260,100, fill="red")


#Creación de canvas
c= Canvas(frame_grafica, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)



#graficación
x= 10
y=10
for i in range(100):
    circulo = c.create_oval(x,y,x+20, y+20 )
    x = random.randint(0, BASE-20)
    y = random.randint(0, ALTURA-20)
    color = "#"
    for caracter in range(6):
        color = color + random.choice ("0123456789ABCDF")
    circulo = c.create_oval(x,y, x + 20, y + 20, fill = color)





ventana_principal.mainloop()