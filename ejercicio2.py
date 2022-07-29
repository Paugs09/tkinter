# Se importa la librería tkinter con todas sus funciones 
from tkinter import *
from tkinter import messagebox

# -------------------
# funciones de la app
# -------------------

def sumar():
    #messagebox.showinfo("Suma 1.0" ,"Hizo click en el botón sumar")
    c=int(a.get()) + int(b.get())
    t_resultados.insert(INSERT,"La suma de " + a.get() + "+" + b.get() + " es = " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")


def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()


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
ventana_principal.config(bg="blue")

# ------------------
# variables globales
# ------------------

a= StringVar()
b= StringVar()
c= StringVar()

#--------------
# frame entrada
# -------------- 
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2",width=780, height=240)
frame_entrada.place(x=10,y=10)


# Etiqueta para el título de la app
titulo = Label(frame_entrada, text="Colegio San José de Guanentá") 
titulo.config(bg="yellow" , fg="blue" , font=("Arial, 16"))
titulo.place(x=390 , y=10)

# Etiqueta para el subtítulo de la app
subtitulo = Label(frame_entrada, text="Especialidad en Sistemas") 
subtitulo.config(bg="yellow" , fg="blue" , font=("Arial, 12"))
subtitulo.place(x=390 , y=40)

# Etiqueta para el subtítulo2 de la app
subtitulo2 = Label(frame_entrada, text="SUMA DE DOS ENTEROS") 
subtitulo2.config(bg="ivory2" , fg="blue" , font=("Arial, 15"))
subtitulo2.place(x=390 , y=70)

# Imagen - logo de la app
logo=PhotoImage(file="sumita3.png")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10,y=10)

# Etiqueta para valor a 
etiq_a= Label(frame_entrada, text ="a = ")
etiq_a.config(bg="ivory2" , fg="blue" , font=("Arial, 20"), anchor=CENTER)
etiq_a.place(x=390, y=120)

# entry para el valor a
entry_a= Entry(frame_entrada , width=4, textvariable=a)
entry_a.config(font=("Arial, 20"), justify=CENTER)
entry_a.focus_set()
entry_a.place (x=487,y=120)

# Etiqueta para valor b
etiq_b= Label(frame_entrada, text ="b = ")
etiq_b.config(bg="ivory2" , fg="blue" , font=("Arial, 20"), anchor=CENTER)
etiq_b.place(x=585, y=120)

# entry para el valor b
entry_b= Entry(frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial, 20"), justify=CENTER)
entry_b.place (x=682,y=120)

#--------------
# frame operaciones
# -------------- 
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="ivory2",width=780, height=120)
frame_operaciones.place(x=10,y=260)

# Botón sumar
bt_sum=PhotoImage(file="bt_sum.png")
#boton_sumar= Button(frame_operaciones, text ="Sumar", width=10)
bt_sumar = Button(frame_operaciones, image= bt_sum, width=105, height= 105, command=sumar)
bt_sumar.place(x=116,y=7)

# Botón borrar
bt_bor= PhotoImage(file="bt_bor.png")
#boton_borrar= Button(frame_operaciones, text ="Borrar", width=10)
boton_borrar = Button(frame_operaciones, image= bt_bor, width=105, height= 105, command=borrar)
boton_borrar.place(x=337,y=7)

# Botón salir
bt_sal=PhotoImage(file="bt_sal.png")
#boton_salir= Button(frame_operaciones, text ="Salir", width=10)
boton_salir = Button(frame_operaciones, image= bt_sal, width=105, height= 105, command=salir)
boton_salir.place(x=558,y=7)

#--------------
# frame resultados
# -------------- 
frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="ivory2",width=780, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para resultados
t_resultados= Text(frame_resultados, width=55, height=3)
t_resultados.config(bg="Skyblue1", fg="black", font=("Arial", 19))
t_resultados.pack()

# se ejecuta el método mainloop de la clase TK a través de la instancia ventana_principal. Este método despliega una ventana simple en pantalla y que da a la espera de lo que el usuario haga, por ejemplo, clic en un botón, escribir en una caja de texto, etc. Cada acción del usuario se  conoce como un evento. El método mainloop es un bucle infinito. 
ventana_principal.mainloop()



