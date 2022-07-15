from tkinter import *

ventana_principal=Tk()

ventana_principal.title("Bandera Noruega")

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
# frame cruzb
# -------------- 
frame_cruzb=Frame(ventana_principal)
frame_cruzb.config(bg="white",width=60, height=480)
frame_cruzb.place(x=150,y=10)

#--------------
# frame cruzb2
# -------------- 
frame_cruzb2=Frame(ventana_principal)
frame_cruzb2.config(bg="white",width=780, height=60)
frame_cruzb2.place(x=10,y=230)

#--------------
# frame cruz1
# -------------- 
frame_cruz1=Frame(ventana_principal)
frame_cruz1.config(bg="navy",width=30, height=480)
frame_cruz1.place(x=165,y=10)

#--------------
# frame cruz2
# -------------- 
frame_cruz2=Frame(ventana_principal)
frame_cruz2.config(bg="navy",width=780, height=30)
frame_cruz2.place(x=10,y=245)



ventana_principal.mainloop()
