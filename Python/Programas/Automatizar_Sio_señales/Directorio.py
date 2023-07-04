from tkinter import filedialog, Tk


def obtener_directorio():
  root = Tk()
  root.withdraw()

  folder_path = filedialog.askdirectory()
  print("Ruta de la carpeta seleccionada:", folder_path)

  root.destroy()
  return folder_path
