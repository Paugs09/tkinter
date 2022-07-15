from tkinter import *

ventana_principal=Tk()

ventana_principal.title("Bandera Suiza")

ventana_principal.geometry('800x500')

ventana_principal.resizable(0,0)

ventana_principal.config(bg="white")

#--------------
# frame entrada
# -------------- 
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red",width=780, height=480)
frame_entrada.place(x=10,y=10)

#--------------
# frame cruz1
# -------------- 
frame_cruz1=Frame(ventana_principal)
frame_cruz1.config(bg="white",width=100, height=350)
frame_cruz1.place(x=340,y=65)

#--------------
# frame cruz2
# -------------- 
frame_cruz2=Frame(ventana_principal)
frame_cruz2.config(bg="white",width=350, height=100)
frame_cruz2.place(x=215,y=190)

ventana_principal.mainloop()
