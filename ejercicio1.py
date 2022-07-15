# Se importa la librería tkinter con todas sus funciones 
from tkinter import *
#----------------
#Ventana principal
#-----------------

#Se declara una variable llamada ventana principal y adquiere las caraacterísticas de un objeto TK.
ventana_principal=Tk()
#Título de la ventana
ventana_principal.title("María Paula Gómez")
# Establecer tamaño a la ventana,
ventana_principal.geometry('1000x500')

# Se ejecuta el método mainloop de la clase TK a través de la instancia ventana_principal. Este método despliega una ventana simple en pantalla y que da a la espera de lo que el usuario haga, por ejemplo, clic en un botón, escribir en una caja de texto, etc. Cada acción del usuario se  conoce como un evento. El método mainloop es un bucle infinito. 
ventana_principal.mainloop()


