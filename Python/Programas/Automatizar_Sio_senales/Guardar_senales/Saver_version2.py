from os import path, chdir
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Encontrar ruta de el webdriver y abrir una ventana

chdir(path.dirname(path.dirname(path.abspath(__file__))))
driver = webdriver.Chrome(executable_path="chromedriver")
driver.maximize_window()

# Definir la ruta a abrir y abrirla

url = "https://siofiltrosinais.com/cataloger"
driver.get(url)

# Cerrar anuncio principal

try:
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@onclick='closeModal()']")))
  div = driver.find_element(by=By.XPATH, value="//div[@onclick='closeModal()']")
  print("Cerrando anuncio...\n")
  div.click()
except:
  print("No se encontró el anuncio\n")

# Elegir idioma

idiomas = ["English", "Español", "Português"]

for indice, idioma in enumerate(idiomas, start=1):
  print(f"{indice}. {idioma}")

while True:
  try:
    eleccion = int(input("\nElige un idioma: "))
    idioma = idiomas[eleccion - 1]
    if eleccion > 0 and eleccion <= 3:
      break
  except:
    print("Opción inválida.")

# Cambiando idioma

try:
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{idioma}s']")))
  select_languaje = driver.find_element(by=By.XPATH, value=f"//option[text()='{idioma}']")
  print("\nCambiando idioma...")
  select_languaje.click()
except:
  print("Error al cambiar el idioma... El idioma no fue encontrado no hay problemas de conexión...\n")

# Eligiendo pares

try:
  WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')))
  select_pair = driver.find_element(by=By.XPATH, value='//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')
  print("Seleccionando pares...")
  select_pair.click()
except:
  print("Error seleccionar los pares...")




