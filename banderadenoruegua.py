# se importa la libreria tkinter con todas las funciones
from tkinter import *



#-----------------------
#funciones de la app
#----------------------


#------------------------------
#ventana principal del programa
#------------------------------

#se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk

ventana_principal = Tk()

# titulo de la ventana

ventana_principal.title("sistemas uis socorro")

#tamaño de la ventana
ventana_principal.geometry("700x500")

# deshabilitar de 
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg="grey99")

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="red" ,width= 150, height=200 )
Frame_entrada.place(x=0,y=0)

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="red" ,width= 150, height=210 )
Frame_entrada.place(x=0,y=300)

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="red" ,width= 500, height=210 )
Frame_entrada.place(x=200,y=0)

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="red" ,width= 500, height=210 )
Frame_entrada.place(x=200,y=200)

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="blue4" ,width= 700, height=50 )
Frame_entrada.place(x=0,y=230)

#-------------------------------------
#frame entrada datos
#-------------------------------------


Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="blue4" ,width= 50, height=700 )
Frame_entrada.place(x=190,y=0)


#run
# se ejecuta la funcion metodo (mainloop) de la claase tk
# este metodo desplaza una ventana simple en la pantalla y queda a la espera de lo que el usuario haga cada accion del usuario se conoce como evento el metodo mainloop es un bucle infinito
#  
ventana_principal.mainloop()