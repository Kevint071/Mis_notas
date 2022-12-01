from tkinter import Tk, Canvas, Label, Entry, Button, Toplevel, Frame, font, END, Listbox
import psycopg2

palabras_traducidas = {}


def limpiar_input(*entry):
    for i in entry:
        i.delete(0, END)


def guardar_palabras(palabra, traduccion):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Torrecilla", host="localhost", port=5432)

    cursor = conn.cursor()
    query = '''INSERT INTO palabras(palabra, traduccion) VALUES (%s, %s)'''
    cursor.execute(query, (palabra, traduccion))
    print("Datos guardados")
    conn.commit()
    conn.close()


def abrir_ventana_agregar():
    """Funcion que abre una nueva ventana para agregar palabras en ingles
       returns None"""

    ventana_agregar = Toplevel()
    ventana_agregar.title("Agregar palabras a base de datos")
    ventana_agregar.resizable(0, 0)

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

    boton_1 = Button(ventana_agregar, text="Guardar", width=9, font=estilo_botones, command=lambda: (guardar_palabras(entry_ingles.get(), entry_traducir.get()),limpiar_input(entry_traducir, entry_ingles)))
    boton_1.place(x=220, y=170)

    # Salir

    boton_salir = Button(ventana_agregar, text="Salir", command=ventana_agregar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=220, y=220)


def abrir_ventana_mostrar():
    """Funcion que abre una nueva ventana para mostrar palabras en ingles
       returns None"""

    ventana_mostrar = Toplevel()
    ventana_mostrar.resizable(0, 0)

    canvas = Canvas(ventana_mostrar, width=500, height=380)
    canvas.pack()

    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Conectar con base de datos

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Torrecilla", host="localhost", port=5432)

    cursor = conn.cursor()
    query = '''SELECT * FROM palabras'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(ventana_mostrar, width=20, height=5)
    listbox.place(x= 180, y = 100)

    for x in row:
        listbox.insert(END, x)
        palabras_traducidas[x[1]] = x[2]

    conn.commit()
    conn.close()

    # Título

    label = Label(ventana_mostrar, text="Lista palabras", font=("Comic sans Ms", 20))
    label.place(x=160, y=20)

    # Salir

    boton_salir = Button(ventana_mostrar, text="Salir", command=ventana_mostrar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=210, y=220)


def run():

    root = Tk()
    root.title("Palabras de ingles")
    root.resizable(0, 0)

    # Canvas principal

    canvas = Canvas(root, height=380, width=490)
    canvas.pack()

    # Título principal

    estilo_label = font.Font(family="Bahnschrift", size=12)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    label = Label(text="Inicio", font=("Comic sans Ms", 20))
    label.place(x=220, y=20)

    # Entrada 1

    label = Label(root, text="Mostrar palabras agregadas: ", font=estilo_label)
    label.place(x=66, y=80)

    boton_editar = Button(root, text="Mostrar", width= 9, font=estilo_botones, command=lambda: abrir_ventana_mostrar())
    boton_editar.place(x=296, y= 78)

    # Entrada 2

    label = Label(root, text="Anadir nueva palabra: ", font=estilo_label)
    label.place(x=117, y=120)

    boton_agregar = Button(root, text="Agregar", command=abrir_ventana_agregar, font=estilo_botones, width=9)
    boton_agregar.place(x=295, y= 118)

    # Entrada 3

    label = Label(root, text="Editar palabras agregadas: ", font=estilo_label)
    label.place(x=77, y=160)

    boton_editar = Button(root, text="Editar", width= 9, font=estilo_botones)
    boton_editar.place(x=296, y= 158)

    # Entrada 4

    label = Label(root, text="Borrar palabras agregadas: ", font=estilo_label)
    label.place(x=77, y=200)

    boton_editar = Button(root, text="Borrar", width= 9, font=estilo_botones)
    boton_editar.place(x=296, y= 198)

    # Salida

    boton_salir = Button(root, text="Salir", command=root.destroy, width=6, font=estilo_botones)
    boton_salir.place(x=220, y=260)

    root.mainloop()

if __name__ == "__main__":
    run()