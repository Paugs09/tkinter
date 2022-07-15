from tkinter import *

ventana_principal=Tk()

ventana_principal.title("Bandera Nigeria")

ventana_principal.geometry('800x500')

ventana_principal.resizable(0,0)

ventana_principal.config(bg="white")

#--------------
# frame entrada
# -------------- 
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="green",width=780, height=480)
frame_entrada.place(x=10,y=10)

#--------------
# frame cruzb
# -------------- 
frame_cruzb=Frame(ventana_principal)
frame_cruzb.config(bg="white",width=260, height=480)
frame_cruzb.place(x=260,y=10)






ventana_principal.mainloop()
