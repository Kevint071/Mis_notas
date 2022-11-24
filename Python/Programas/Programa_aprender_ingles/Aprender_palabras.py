from tkinter import Tk, Canvas, Label, Entry, Button, Toplevel, Frame, font, END
import psycopg2

def limpiar_input(entry):
    pass




# Funcion para abrir ventana "Agregar palabras"

def abrir_ventana_agregar():
    ventana_agregar = Toplevel()
    ventana_agregar.title("Agregar palabras a base de datos")

    canvas = Canvas(ventana_agregar, width=500, height=380)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=12)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Título

    label = Label(ventana_agregar, text="Agregar palabra", font=("Comic sans Ms", 20))
    label.place(x=150, y=20)

    # Entrada 1

    label = Label(ventana_agregar, text="Añade la palabra en ingles: ", font=estilo_label)
    label.place(x=70, y=90)

    entry_ingles = Entry(ventana_agregar)
    entry_ingles.place(x=300, y=90)

    # Entrada 2

    label = Label(ventana_agregar, text="Añade la traducción de la palabra: ", font=estilo_label)
    label.place(x=20, y=120)

    entry_traducir = Entry(ventana_agregar)
    entry_traducir.place(x=300, y=120)

    boton_1 = Button(ventana_agregar, text="Guardar", width=9, font=estilo_botones, command=lambda: (entry_traducir.delete(0, END), entry_ingles.delete(0, END)))
    boton_1.place(x=220, y=170)

    # Salir

    boton_salir = Button(ventana_agregar, text="Salir", command=ventana_agregar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=220, y=220)


def run():

    root = Tk()
    root.title("Palabras de ingles")

    # Canvas principal

    canvas = Canvas(root, height=380, width=500)
    canvas.pack()

    # Título principal

    estilo_label = font.Font(family="Bahnschrift", size=12)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    label = Label(text="Inicio", font=("Comic sans Ms", 20))
    label.place(x=220, y=20)

    # Entrada 1

    label = Label(root, text="Anadir nueva palabra: ", font=estilo_label)
    label.place(x=117, y=80)

    boton_agregar = Button(root, text="Agregar", command=abrir_ventana_agregar, font=estilo_botones, width=9)
    boton_agregar.place(x=295, y= 78)

    # Entrada 2

    label = Label(root, text="Editar palabras agregadas: ", font=estilo_label)
    label.place(x=77, y=120)

    boton_editar = Button(root, text="Editar", width= 9, font=estilo_botones)
    boton_editar.place(x=296, y= 118)

    boton_salir = Button(root, text="Salir", command=root.destroy, width=6, font=estilo_botones)
    boton_salir.place(x=230, y=220)

    root.mainloop()

if __name__ == "__main__":
    run()