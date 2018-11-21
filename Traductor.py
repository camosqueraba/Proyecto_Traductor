from tkinter import *

ventana = Tk()
ventana.title('TRADUCTOR CON PARSER PLY')
ventana.resizable(0, 0)
# ventana.iconbitmap('icon.jgp')

# Le pasamos el valor root, para meter el frame dentro de la raíz
frame = Frame(ventana, width=700, height=400)
# Side para la posición y anchor para anclarlo arriba y con "W" al oeste
frame.pack(side="top", anchor="w")
# Rellenar en horizontal y vertical y expanda el frame en todo lo que ocupe el padre
frame.pack(fill="both", expand=True)
frame.config(cursor="arrow")
# frame.config(bg="#f6085e")


# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")



label_ingles = Label(frame, text="INGLÉS")
label_ingles.grid(row=0, column=0)
label_ingles.config(fg="blue", font=("Verdana", 24))
#label_ingles.config(textvariable='Ingles')

# Mostrar una imagen como etiqueta

imagen = PhotoImage(file="imagenes/imagen-fondo.png")
label_imagen = Label(frame, image=imagen, bd=0)
label_imagen.grid(row=0, column=1)


label_español = Label(frame, text="ESPAÑOL")
label_español.grid(row=0, column=2)
label_español.config(fg="red", font=("Verdana", 24))
#label_español.config(textvariable='Ingles')

texto_ingles = Text(frame)
texto_ingles.config(width=30, height=10, font=("Consolas",12))
texto_ingles.grid(row=1,column=0)



texto_español = Text(frame)
texto_español.config(width=30, height=10, font=("Consolas",12))
texto_español.grid(row=1,column=2)


ventana.mainloop()
