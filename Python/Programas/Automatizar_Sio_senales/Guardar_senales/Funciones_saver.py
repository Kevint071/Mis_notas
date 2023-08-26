from os import path, chdir
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException
from time import sleep

# Agregar a ejecutar_navegador() si no se quiere mostrar el navegador

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)

def ejecutar_navegador():
    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")

    # Encontrar ruta de el webdriver y abrir una ventana
    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://siofiltrosinais.com/cataloger"
    driver.get(url)
    sleep(1)


def retroceder_a_catalogador():
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="screenshot"]/div/a')))
        retroceder = driver.find_element(by=By.XPATH, value='//*[@id="screenshot"]/div/a')
        print("Retrocediendo...")
        retroceder.click()
    except:
        print("No se pudo retroceder...\n")


def cerrar_anuncio():
    # Cerrar anuncio principal
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@onclick='closeModal()']")))
        div = driver.find_element(by=By.XPATH, value="//div[@onclick='closeModal()']")
        print("Cerrando anuncio...\n")
        div.click()
    except:
        print("No se encontró el anuncio\n")


def elegir_idioma():
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
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{idioma}']")))
        select_languaje = driver.find_element(by=By.XPATH, value=f"//option[text()='{idioma}']")
        print("\nCambiando idioma...\n")
        select_languaje.click()
    except:
        print("Error al cambiar el idioma... El idioma no fue encontrado no hay problemas de conexión...\n")


def seleccionar_mercado():
    # Seleccionando dropdown de mercados

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')))
        select_dropdown = driver.find_element(by=By.XPATH, value='//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]')
        select_dropdown.click()
    except:
        print("Error seleccionar los pares...")
    sleep(0.1)

    # Eligiendo el mercado de opciones binarias

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[text()='BINÁRIAS']")))
        opcion_binarias = driver.find_element(by=By.XPATH, value="//*[text()='BINÁRIAS']")
        opcion_binarias.click()
    except:
        print("Error al seleccionar la opción binaria...")
    
    # Eligiendo el mercado de opciones digitales
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[text()='DIGITAIS']")))
        opcion_binarias = driver.find_element(by=By.XPATH, value="//*[text()='DIGITAIS']")
        opcion_binarias.click()
        select_dropdown.click()
    except:
        print("Error al seleccionar la opción digital..")


def obtener_inputs():
  # Obteniendo elementos input
  try:
      WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@class,'bg-[#222f3e]')]")))
      global elementos_input
      elementos_input = driver.find_elements(by=By.XPATH, value="//input[contains(@class,'bg-[#222f3e]')]")
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
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[4]/div/select")))
      dropdown_direccion = driver.find_element(by=By.XPATH, value="//div[4]/div/select")
      dropdown_direccion.click()
  except:
      print("Error al desplegar el dropdown\n")

  # Agregando direccion call y put
      
  try:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[4]/div/select/option[3]")))
      option_call_put = driver.find_element(by=By.XPATH, value="//div[4]/div/select/option[3]")
      option_call_put.click()
  except:
      print("Error al agregar la dirección\n")


def agregar_timeframe(timeframe):
  # Desplegando el Dropdown de los timeframe
  try:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[5]/div/select")))
      dropdown_timeframe = driver.find_element(by=By.XPATH, value="//div[4]/div/select")
      dropdown_timeframe.click()
  except:
      print("Error al desplegar el dropdown\n")

  # Agregando timeframe
      
  try:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//option[@value='{timeframe}']")))
      option_timeframe = dropdown_timeframe.find_element(by=By.XPATH, value=f"//option[@value='{timeframe}']")
      option_timeframe.click()
  except:
      print("Error al agregar el timeframe\n")


def agregar_dia(dia):
    # Agregando los dias de efectividad
    try:
        input_dia = elementos_input[1]
        input_dia.click()
        sleep(0.1)
        input_dia.clear()
        sleep(0.1)
        input_dia.send_keys(f"{dia}")
    except:
        print('No se pudo agregar el dia...\n')


def filtrar_noticias():
    # Presionando el input de filtrar noticias
    try:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "filter")))
      input_filtrar = elementos_input[2]
      input_filtrar.click()
    except:
        print("No se pudo seleccional el input de filtrar noticias...\n")


def iniciar_catalogacion():
    # Se preciona el boton iniciar
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[9]/button")))
        boton_iniciar = driver.find_element(By.XPATH, value="//div[9]/button")
        print("Iniciando catalogación...")
        boton_iniciar.click()
    except:
        print("Hubo un error al iniciar la catalogación...\n")


def obtener_senales():
    # Obtener las señales que estan en el textarea
    # try:
    WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    print("Obteniendo señales...\n")
    senales = textarea.get_attribute("value")
    if senales == "":
        print("No hay señales en esta catalogación...")
        return None
    return senales
    # except:
    #     print("No se pudo obtener el textarea ni su contenido...\n")

sleep(1)
