import tkinter as tk
from tkinter import ttk

def seleccionar_libro(libro):
    print("Libro seleccionado:", libro)


def elegir_libro():
    ventana = tk.Tk()
    ventana.title("Seleccionar Libro de la Biblia")

    # Lista de libros de la Biblia
    libros_biblia = [
        "Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio", 
        "Josué", "Jueces", "Rut", "1 Samuel", "2 Samuel", "1 Reyes", 
        "2 Reyes", "1 Crónicas", "2 Crónicas", "Esdras", "Nehemías", 
        "Ester", "Job", "Salmos", "Proverbios", "Eclesiastés", "Cantares",
        "Isaías", "Jeremías", "Lamentaciones", "Ezequiel", "Daniel", 
        "Oseas", "Joel", "Amós", "Abdías", "Jonás", "Miqueas", "Nahúm", 
        "Habacuc", "Sofonías", "Hageo", "Zacarías", "Malaquías", 
        "Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", 
        "1 Corintios", "2 Corintios", "Gálatas", "Efesios", "Filipenses", 
        "Colosenses", "1 Tesalonicenses", "2 Tesalonicenses", 
        "1 Timoteo", "2 Timoteo", "Tito", "Filemón", "Hebreos", "Santiago", 
        "1 Pedro", "2 Pedro", "1 Juan", "2 Juan", "3 Juan", "Judas", "Apocalipsis"
    ]

    # Variable para almacenar la selección del usuario
    libro_seleccionado = tk.StringVar()

    # Crear el OptionMenu
    opcion_libros = ttk.OptionMenu(ventana, libro_seleccionado, libros_biblia[0], *libros_biblia, command=lambda: (seleccionar_libro()))
    opcion_libros.pack(padx=10, pady=10)

    ventana.mainloop()

elegir_libro()