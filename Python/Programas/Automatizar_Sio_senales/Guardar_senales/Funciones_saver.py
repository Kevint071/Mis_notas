from os import path, chdir
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def ejecutar_navegador():

    # Encontrar ruta de el webdriver y abrir una ventana
    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://siofiltrosinais.com/cataloger"
    driver.get(url)
    sleep(1)


def retroceder_a_catalogador():
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='screenshot']/div/a/button")))
        retroceder = driver.find_element(by=By.XPATH, value="//*[@id='screenshot']/div/a/button")
        print("Retrocediendo...")
        retroceder.click()
    except:
        print("No se pudo retroceder...\n")


def cerrar_anuncio():
    # Cerrar anuncio principal
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@onclick='closeModal()']")))
        div = driver.find_element(by=By.XPATH, value="//div[@onclick='closeModal()']")
        print("Cerrando anuncio...\n")
        div.click()
    except:
        print("No se encontró el anuncio\n")


def elegir_idioma():
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{idioma}']")))
        select_languaje = driver.find_element(by=By.XPATH, value=f"//option[text()='{idioma}']")
        print("\nCambiando idioma...")
        select_languaje.click()
    except:
        print("Error al cambiar el idioma... El idioma no fue encontrado no hay problemas de conexión...\n")


def seleccionar_mercado():
    # Seleccionando dropdown de mercados

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')))
        select_dropdown = driver.find_element(by=By.XPATH, value='//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')
        print("Seleccionando pares...")
        select_dropdown.click()
    except:
        print("Error seleccionar los pares...")

    # Eligiendo el mercado de opciones binarias

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='BINÁRIAS']")))
        opcion_binarias = driver.find_element(by=By.XPATH, value="//*[text()='BINÁRIAS']")
        print("Seleccionando binárias...")
        opcion_binarias.click()
        select_dropdown.click()
    except:
        print("Error al seleccionar la opción binaria...")


def obtener_inputs():
  # Obteniendo elementos input
  try:
      WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@class,'bg-[#222f3e]')]")))
      global elementos_input
      elementos_input = driver.find_elements(by=By.XPATH, value="//input[contains(@class,'bg-[#222f3e]')]")
      print("Obteniendo inputs...")
  except:
      print("Error al obtener inputs\n")


def agregar_efectividad(num):
  # Clickeando el input de porcentaje de efectividad

  try:
      input_efectividad = elementos_input[0]
      input_efectividad.click()
  except:
      print("Error al clickear el input de efectividad...\n")

  # Digitando el porcentaje de efectividad
  input_efectividad.send_keys(f"{num}")


def agregar_direccion_op():
  # Desplegando el Dropdown de las direcciones
  try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[4]/div/select")))
      dropdown_direccion = driver.find_element(by=By.XPATH, value="//div[4]/div/select")
      print("Desplegando dropdown...")
      dropdown_direccion.click()
  except:
      print("Error al desplegar el dropdown\n")

  # Agregando direccion call y put
      
  try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[4]/div/select/option[3]")))
      option_call_put = driver.find_element(by=By.XPATH, value="//div[4]/div/select/option[3]")
      print("Agregando dirección...")
      option_call_put.click()
      dropdown_direccion.click()
  except:
      print("Error al agregar la dirección\n")

sleep(1)
