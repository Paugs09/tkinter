# Se importa la librería tkinter con todas sus funciones 
from tkinter import *
#----------------
# ventana principal
#-----------------

#Se declara una variable llamada ventana principal y adquiere las caraacterísticas de un objeto TK.
ventana_principal=Tk()

#Título de la ventana
ventana_principal.title("María Paula Gómez")

# Establecer tamaño a la ventana,
ventana_principal.geometry('800x500')

#Desahbilitar el botón de maximizar 
ventana_principal.resizable(0,0)

# Color de fondo de la ventana principal
ventana_principal.config(bg="white")

#--------------
# frame entrada
# -------------- 
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="yellow",width=780, height=240)
frame_entrada.place(x=10,y=10)

#--------------
# frame operaciones
# -------------- 
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue",width=780, height=120)
frame_operaciones.place(x=10,y=250)

#--------------
# frame resultados
# -------------- 
frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="red",width=780, height=120)
frame_resultados.place(x=10,y=370)

# se ejecuta el método mainloop de la clase TK a través de la instancia ventana_principal. Este método despliega una ventana simple en pantalla y que da a la espera de lo que el usuario haga, por ejemplo, clic en un botón, escribir en una caja de texto, etc. Cada acción del usuario se  conoce como un evento. El método mainloop es un bucle infinito. 
ventana_principal.mainloop()



