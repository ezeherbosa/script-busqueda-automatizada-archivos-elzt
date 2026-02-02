🔍 Bot de Búsqueda Automatizada - Justice.gov
Este script de Python automatiza el proceso de búsqueda de múltiples nombres en la base de datos pública de documentos del caso Epstein en el sitio oficial del Departamento de Justicia de los EE.UU. (justice.gov).

El bot utiliza Selenium para simular un navegador real, iterar sobre una lista de nombres personalizada y generar un reporte en CSV indicando si se encontraron posibles coincidencias.

📋 Requisitos Previos
Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

Google Chrome: El navegador debe estar instalado en tu computadora.

Python 3.

Nota para usuarios Windows: Al instalar, asegúrate de marcar la casilla "Add Python to PATH".

🚀 Instalación
Descarga el código: Clona este repositorio o descarga los archivos como ZIP y descomprímelos en una carpeta.

Instala las dependencias: Abre una terminal (Símbolo del sistema o PowerShell), navega hasta la carpeta del proyecto y ejecuta:

Bash

pip install selenium webdriver-manager pandas

⚙️ Configuración:

Antes de correr el bot, necesitas crear el archivo con los nombres que quieres investigar.

En la misma carpeta del script, crea un archivo de texto llamado nombres.txt.

Escribe los nombres que deseas buscar, uno por línea, no separes con comas, solo un enter.

Guarda el archivo.

Ejemplo de nombres.txt:

Plaintext

Ghislaine Maxwell
John Doe
Nombre Ejemplo
Nota: Asegúrate de guardar el archivo con codificación UTF-8 si usas caracteres especiales o tildes.

▶️ Ejecución
Para iniciar el bot:

Abre la terminal en la carpeta del proyecto.

Tip para Windows: Entra a la carpeta, escribe cmd en la barra de direcciones de arriba y presiona Enter.

Ejecuta el siguiente comando:

Bash

python buscador.py
El navegador se abrirá automáticamente y verás el progreso en la terminal. Al finalizar, se generará un archivo reporte_final.csv con los resultados.



⚠️ Solución de Problemas Comunes
Error: "No module named...": Significa que no instalaste las librerías correctamente. Repite el paso de "Instalación".

El bot abre el navegador pero no escribe nada: Es posible que el sitio web haya cambiado el identificador de la caja de búsqueda.

Solución: Abre buscador.py y busca la línea driver.find_element(By.ID, "searchInput"). Es posible que debas cambiar "searchInput" por "edit-keys" (el ID estándar de sitios Drupal gubernamentales) u otro ID que encuentres inspeccionando la web.

El navegador se cierra inmediatamente: Asegúrate de tener Google Chrome actualizado.




⚖️ Aviso Legal y Ético
Este software es para fines educativos y de investigación periodística o personal.

La información consultada es de dominio público.

El script incluye pausas (time.sleep) para evitar saturar el servidor del sitio web. No elimines estas pausas, ya que podrías ser bloqueado por el servidor.

Autor: Ezeherbosa

Script armado en base un posteo de una usuaria en X / Tw.

Gracias Gemini y google.

Disclaimer: los nombres que se encuentren en la lista a modo de ejemplo fueron meramente azar o coincidencia
