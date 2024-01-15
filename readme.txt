Sistema de Análisis de Emociones README
Este README proporciona instrucciones para configurar y ejecutar el sistema de análisis de emociones. El sistema consta de un frontend en React y un backend en Django, utilizando la API de Hugging Face para el análisis de emociones.

Configuración del Entorno
Frontend
Abre una terminal y navega hasta la carpeta front.

Ejecuta el siguiente comando para instalar las dependencias:

bash
Copy code
npm install
Después de la instalación, inicia el servidor de desarrollo con:

bash
Copy code
npm run dev
Accede al frontend en tu navegador visitando http://localhost:3000.

Backend
Abre otra terminal y navega hasta la carpeta back.

Instala las dependencias de Python con:

bash
Copy code
pip install -r requirements.txt
Crea un archivo .env en la carpeta back y agrega tu token de Hugging Face:

env
Copy code
TOKEN_HUGGINGFACE=tu_token_aqui
Ejecuta el servidor Django con:

bash
Copy code
python manage.py runserver
El backend estará disponible en http://localhost:8000.

Dockerización (opcional)
Nota: Se medio configuro el Docker Compose, no lo probe ya que tuve problemas con  WSL. A

Asegúrate de tener Docker instalado.

En la raíz del proyecto, ejecuta:

bash
Copy code
docker-compose up
El frontend estará disponible en http://localhost:3000 y el backend en http://localhost:8000.

Notas Adicionales
La API puede generar resultados de archivos CSV pequeños. Ten en cuenta que la API de Hugging Face puede poner en espera las solicitudes después de cierto límite. Tendria que   manejar esta situación en el código, como esperar antes de realizar más solicitudes.

La configuración para la API en tiempo real utilizando WebSockets no se ha implementado en esta versión. No me dio tiempo para la condiguracion de los channel de django.

