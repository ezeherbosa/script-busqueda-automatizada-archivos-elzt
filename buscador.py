from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os

def iniciar_bot():
    # --- CONFIGURACIÓN ---
    NOMBRE_ARCHIVO_TXT = 'nombres.txt'
    URL_BUSQUEDA = "https://www.justice.gov/epstein/search"
    # ---------------------

    # 1. CARGAR NOMBRES DESDE TXT
    print(f"Leyendo archivo {NOMBRE_ARCHIVO_TXT}...")

    if not os.path.exists(NOMBRE_ARCHIVO_TXT):
        print(f"ERROR: No encuentro el archivo '{NOMBRE_ARCHIVO_TXT}'.")
        exit()

    try:
        with open(NOMBRE_ARCHIVO_TXT, 'r', encoding='utf-8') as archivo:
            nombres = [linea.strip() for linea in archivo if linea.strip()]
        print(f"Se cargaron {len(nombres)} nombres.")

    except Exception as e:
        print(f"Error leyendo el archivo: {e}")
        exit()

    # 2. INICIAR NAVEGADOR
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    resultados = []

    print("Abriendo navegador...")

    for nombre in nombres:
        try:
            driver.get(URL_BUSQUEDA)
            time.sleep(2) # Espera a que cargue la página inicial

            # --- NUEVO: VERIFICACIÓN "I AM NOT A ROBOT" ---
            try:
                # Buscamos el botón por su texto exacto (value)
                boton_robot = driver.find_element(By.XPATH, "//input[@value='I am not a robot']")
                if boton_robot.is_displayed():
                    print("--> Botón de verificación detectado. Clickeando...")
                    boton_robot.click()
                    time.sleep(3) # Damos tiempo extra para que la página se "desbloquee" o recargue
            except:
                # Si no encuentra el botón, significa que entró directo al buscador.
                pass
            # -----------------------------------------------

            # 3. BUSCAR LA CAJA DE TEXTO
            # Nota: Si tras el click la página cambia, el ID podría ser 'edit-keys' o 'searchInput'.
            # He dejado 'searchInput' como tenías, pero si falla, prueba cambiarlo a 'edit-keys'.
            try:
                caja_busqueda = driver.find_element(By.ID, "searchInput")
            except:
                # Intento secundario por si el ID es diferente
                caja_busqueda = driver.find_element(By.ID, "edit-keys")

            caja_busqueda.clear()
            caja_busqueda.send_keys(nombre)
            caja_busqueda.send_keys(Keys.RETURN)

            time.sleep(3) # Esperar resultados

            # 4. ANALIZAR RESULTADOS
            cuerpo_pagina = driver.find_element(By.TAG_NAME, "body").text.lower()

            if "no results found" in cuerpo_pagina or "su búsqueda no produjo resultados" in cuerpo_pagina:
                print(f"[-] {nombre}: No encontrado")
                hallazgo = False
            else:
                print(f"[+] {nombre}: Posible coincidencia")
                hallazgo = True

            resultados.append({'Nombre': nombre, 'Encontrado': hallazgo})

        except Exception as e:
            print(f"[ERROR] Con {nombre}: {e}")

    driver.quit()

    # 5. GUARDAR RESULTADOS
    df_output = pd.DataFrame(resultados)
    df_output.to_csv('reporte_final.csv', index=False)
    print("--- Búsqueda finalizada. Archivo 'reporte_final.csv' creado. ---")

if __name__ == "__main__":
    iniciar_bot()