from os import chdir, path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# from selenium.webdriver.chrome.options import Options

# Agregar a ejecutar_navegador() si no se quiere mostrar el navegador
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)


def ejecutar_navegador():

    # Encontrar ruta de el webdriver y abrir una ventana
    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://siofiltrosinais.com/trend"
    driver.get(url)
    sleep(1)

def retroceder_a_filtrador():
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

def agregar_senales_textarea():
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.TAG_NAME, "textarea"))
        textarea = driver.find_element(By.TAG_NAME, value="textarea")
        textarea.click()
        textarea.send_keys()
    except:
        print("No se agregaron las señales...\n")