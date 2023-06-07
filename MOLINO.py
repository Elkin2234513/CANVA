from tkinter import *
import random

#variables globales
BASE = 460
ALTURA = 220
RADIO = 45

#funcion para modificar arco
def modificar_arco(angulo):
    angulo2 = int(angulo)+90
    angulo3= int(angulo)+180
    angulo4= int(angulo)+270
    c.itemconfig(arco, start = angulo) 
    c.itemconfig(arco1, start = angulo2) 
    c.itemconfig(arco2, start = angulo3) 
    c.itemconfig(arco3, start = angulo4) 


#ventana principal
ventana_principal = Tk()

ventana_principal.title("ELKIN REX")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

#frame de graficacion
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="green", width=480, height=240)
frame_grafica.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_grafica, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

triangulo = c.create_polygon(BASE/2, ALTURA/2, BASE/2 + 30, ALTURA,BASE/2-30, ALTURA, fill ="white" )

arco = c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start = 0, extent = 45, fill = "blue")
arco1 = c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start = 90, extent = 45, fill = "yellow")
arco2 = c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start = 180, extent = 45, fill = "red")
arco3 = c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start = 270, extent = 45, fill = "purple")


#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)
#barra de desplazamiento
barra_desplazamiento = Scale(frame_controles, label="Angulo", from_=0, to_=360, orient="horizontal", length=470, tickinterval=45, command=modificar_arco)
barra_desplazamiento.pack()

ventana_principal.mainloop()