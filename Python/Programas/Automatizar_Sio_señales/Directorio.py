from tkinter import filedialog, Tk

# Crea una ventana principal oculta
root = Tk()
root.withdraw()

# Abre el cuadro de diálogo de selección de directorio
folder_path = filedialog.askdirectory()

# Imprime la ruta de la carpeta seleccionada
print("Ruta de la carpeta seleccionada:", folder_path)

# Cierra la ventana principal
root.destroy()
