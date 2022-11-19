from tkinter import Tk, Canvas, Frame, Label, Entry
import psycopg2

root = Tk()
root.title("Palabras de ingles")

# Canvas

canvas = Canvas(root, height=380, width=500)
canvas.pack()

# Entrada 1

label = Label(text="Añade la palabra en ingles: ")
label.place(x=77, y=50)

entry_ingles = Entry()
entry_ingles.place(x=240, y=50)

# Entrada 2

label = Label(text="Añade la traducción de la palabra: ")
label.place(x=40, y=80)

entry_traducir = Entry()
entry_traducir.place(x=240, y=80)

root.mainloop()