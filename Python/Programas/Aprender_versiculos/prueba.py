from tkinter import Tk, Canvas, font, Label


def ubicar_eje_x(root, ancho, elemento, porcentaje):
    elemento.place(x=1, y=1)
    root.update_idletasks()
    ancho_elemento = elemento.winfo_width()
    root.after(5, print(ancho_elemento))
    centrar_eje_x = (ancho-ancho_elemento)*porcentaje
    print(centrar_eje_x)

    return centrar_eje_x


def desplegar_interfaz():
    
    # Crear y configurar ventana

    root = Tk()
    root.title("Almacenador Bíblico Pro")
    root.resizable(0, 0)

    alto = 400
    ancho = 500

    canvas = Canvas(root, height=alto, width=ancho)
    canvas.pack()

    # Estilos de tamaño y texto predeterminados

    estilo_label = font.Font(family="Bahnschrift", size=11)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Creando label de inicio

    label = Label(text="Almacenador Bíblico Pro", font=("Comic sans Ms", 15))
    eje_x_label_inicio = ubicar_eje_x(root, ancho, label, 0.5)
    label.place(x=eje_x_label_inicio, y=20)

    # Label pedir libro

    label_pedir_libro = Label(text="Seleccione un libro bíblico: ", font=estilo_label)
    eje_x_label_libro = ubicar_eje_x(root, ancho, label_pedir_libro, 0.18)
    label_pedir_libro.place(x=eje_x_label_libro, y=70)



    root.mainloop()
  
desplegar_interfaz()