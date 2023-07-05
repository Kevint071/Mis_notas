from tkinter import Tk, Canvas, font, Label, Button, Frame

def desplegar_interfaz():
    # Crear y configurar ventana
    root = Tk()
    root.title("Almacenador Bíblico Pro")
    root.resizable(0, 0)

    alto = 400
    ancho = 500

    canvas = Canvas(root, height=alto, width=ancho)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1, rely=0.08, relwidth=0.8, relheight=0.8)


    # Estilos de tamaño y texto predeterminados
    estilo_label = font.Font(family="Bahnschrift", size=11)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Creando label de inicio

    label_version = Label(frame, text="Reina Valera Versión 1960", font=("Comic sans Ms", 14))
    label_version.grid(row=0, column=0, pady=20, sticky="nw")

    # Label pedir libro
    label_pedir_libro = Label(frame, text="Seleccione un libro bíblico: ", font=estilo_label)
    label_pedir_libro.grid(row=1, column=0, sticky="w")

    boton_libro = Button(frame, text="Seleccionar")
    boton_libro.grid(row=1, column=1, padx=10)

    # Label pedir capítulo
    label_pedir_libro = Label(frame, text="Selecciona un capítulo: ", font=estilo_label)
    label_pedir_libro.grid(row=2, column=0, sticky="w")

    boton_libro = Button(frame, text="Seleccionar")
    boton_libro.grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

desplegar_interfaz()
