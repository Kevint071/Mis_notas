from tkinter import Tk, Canvas, font, Label


def desplegar_interfaz():
    root = Tk()
    root.title("Aprender versículos")
    root.resizable(0, 0)

    alto = 400
    ancho = 600

    canvas = Canvas(root, height=alto, width=ancho)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=12)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    label = Label(text="Inicio", font=("Comic sans Ms", 20))
    label.place(x=-1000, y=-100)
    root.update_idletasks()
    ancho_label = label.winfo_width()
    root.after(5, print(ancho_label))
    label.place(x=(ancho-ancho_label)/2, y=20)

    # Obtener el ancho del Label
    

    root.mainloop()