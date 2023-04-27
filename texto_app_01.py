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
ventana_principal.geometry("500x500")

# deshabilitar de 
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg="green")

#run
# se ejecuta la funcion metodo (mainloop) de la claase tk
# este metodo desplaza una ventana simple en la pantalla y queda a la espera de lo que el usuario haga cada accion del usuario se conoce como evento el metodo mainloop es un bucle infinito
#  
ventana_principal.mainloop()