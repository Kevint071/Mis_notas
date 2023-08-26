from tkinter import filedialog, Tk


def obtener_directorio():
  root = Tk()
  root.withdraw()

  folder_path = filedialog.askdirectory()

  root.destroy()
  return folder_path
