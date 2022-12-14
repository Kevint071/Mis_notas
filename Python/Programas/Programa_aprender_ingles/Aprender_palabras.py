from tkinter import Tk, Canvas, Label, Entry, Button, Toplevel, font, END, Listbox, StringVar
import psycopg2
from os import name, system

palabras_traducidas = {}


def verificar_palabras(palabra, label, x, y):
    label.place(x=x, y=y)
    if palabra.count(" ") >= 1:
        if palabra.replace(" ", "").isalpha():
            label["text"] = "✔"
            return True
        else:
            label["text"] = "X"
            return False
    else:
        if palabra.isalpha():
            label["text"] = "✔"
            return True
        elif palabra.isalpha() == False or palabra.len() == 0:
            label["text"] = "X"
            return False


def limpiar_input(*entry):
    for i in entry:
        i.delete(0, END)


def obtener_palabra(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    return row


def buscar_palabras(valor, label):

    """Funcion que busca palabras en la ventana mostrar
       parametros palabra cualquier str, label"""

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Torrecilla", host="localhost", port=5432)

    valor = valor.capitalize()

    query = f"""SELECT palabra, traduccion FROM palabras WHERE palabra='{valor}'"""

    row = obtener_palabra(query, conn)

    if row == None:
        query = f"""SELECT palabra, traduccion FROM palabras WHERE traduccion='{valor}'"""

    row = obtener_palabra(query, conn)
    
    if row == None:
        query = f"""SELECT palabra, traduccion FROM palabras WHERE id='{valor}'"""

    row = obtener_palabra(query, conn)
    mostrar_busqueda(row, label)

    conn.commit()
    conn.close()


def mostrar_busqueda(row, label):

    label["text"] = (f"Resultado: {row[0]} → {row[1]}")



def guardar_palabras(entry_ingles, entry_traducir, ventana_agregar):

    # Obteniendo palabra de las entradas y verificando que no tengan caracteres especiales

    palabra = entry_ingles.get()
    traduccion = entry_traducir.get()

    label_1 = Label(ventana_agregar, font=("Comic sans Ms", 11))
    label_2 = Label(ventana_agregar, font=("Comic sans Ms", 11))
    
    verificacion_palabra = verificar_palabras(palabra, label_1, x=430, y=85)
    verificacion_traducir = verificar_palabras(traduccion, label_2, x=430, y=115)

    if verificacion_palabra and verificacion_traducir:
        limpiar_input(entry_ingles, entry_traducir)
        palabra = palabra.capitalize()
        traduccion = traduccion.capitalize()
    else:
        return None

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

    boton_1 = Button(ventana_agregar, text="Guardar", width=9, font=estilo_botones, command=lambda: (guardar_palabras(entry_ingles, entry_traducir, ventana_agregar)))
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

    estilo_label = font.Font(family="Bahnschrift", size=10)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Conectar con base de datos

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Torrecilla", host="localhost", port=5432)

    cursor = conn.cursor()
    query = '''SELECT * FROM palabras'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(ventana_mostrar, width=40, height=5)
    listbox.place(x= 130, y = 130)

    for x in row:
        listbox.insert(END, x)
        palabras_traducidas[x[1]] = x[2]

    conn.commit()
    conn.close()

    # Título

    label = Label(ventana_mostrar, text="Lista palabras", font=("Comic sans Ms", 20))
    label.place(x=160, y=20)

    # Buscar palabras

    label = Label(ventana_mostrar, text="Buscar palabra:", font=estilo_label)
    label.place(x=130, y=90)

    entry_buscar = Entry(ventana_mostrar)
    entry_buscar.place(x=230, y=92, width=80)

    label_busqueda = Label(ventana_mostrar, font=("Bahnschrift", 10))
    label_busqueda.place(x=160, y=230)

    boton_buscar = Button(ventana_mostrar, text="Buscar", command=lambda: buscar_palabras(entry_buscar.get(), label_busqueda))
    boton_buscar.place(x=320, y=89)

    # Salir

    boton_salir = Button(ventana_mostrar, text="Salir", command=ventana_mostrar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=210, y=270)


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
    label.place(x=72, y=200)

    boton_borrar = Button(root, text="Borrar", width= 9, font=estilo_botones)
    boton_borrar.place(x=296, y= 198)

    # Entrada 5

    label = Label(root, text="Iniciar test: ", font=estilo_label)
    label.place(x=195, y=240)

        # Probando sistema operativo
    
    if name == "posix":
        comando = "python3 ./Estudiar_palabras_verbos_ingles.py"
    elif name == "nt" or name == "dos" or name == "ce":
        comando = "python ./Estudiar_palabras_verbos_ingles.py"

    boton_test = Button(root, text="Iniciar", width= 9, font=estilo_botones, command=lambda: (root.destroy(), system(comando)))
    boton_test.place(x=296, y= 238)

    # Salida

    boton_salir = Button(root, text="Salir", command=root.destroy, width=6, font=estilo_botones)
    boton_salir.place(x=220, y=300)

    root.mainloop()

if __name__ == "__main__":
    run()