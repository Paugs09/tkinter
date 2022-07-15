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
ventana_principal.geometry('800x500')

#Desahbilitar el botón de maximizar 
ventana_principal.resizable(0,0)

# Color de fondo de la ventana principal
ventana_principal.config(bg="plum2")

# Agregamos un widget a la ventana principal
letrero=Label(text='\n\nSistemas, la mejor!!\n\n', bg="plum2")
letrero.pack()

# Agregamos un widget a la ventana principal
letrero2=Label(text='\n\nMaría Paula Gómez\n\n',bg="plum2")
letrero2.pack()

# Agregamos un widget a la ventana principal
letrero3=Label(text='\n\nColegio San José de Guanentá\n\n',bg="plum2")
letrero3.pack()

# Se ejecuta el método mainloop de la clase TK a través de la instancia ventana_principal. Este método despliega una ventana simple en pantalla y que da a la espera de lo que el usuario haga, por ejemplo, clic en un botón, escribir en una caja de texto, etc. Cada acción del usuario se  conoce como un evento. El método mainloop es un bucle infinito. 
ventana_principal.mainloop()



