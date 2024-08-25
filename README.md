# comfama_api

# Instrucciones para Ejecutar la Aplicación con Docker

## Requisitos Previos

- **Docker**: Asegúrate de tener Docker instalado en tu máquina. Puedes descargar e instalar Docker desde [Docker's official website](https://www.docker.com/get-started).

## Construir la Imagen Docker

Para construir la imagen Docker de la aplicación, sigue estos pasos:

1. **Abre una terminal**.

2. **Navega al directorio del proyecto** donde se encuentra el archivo `Dockerfile`.

3. **Ejecuta el siguiente comando** para construir la imagen Docker:

   ```bash
   docker build -t myapp .
   
3. **Ejecuta el siguiente comando** para ejecutar la imagen Docker:

   ```bash
   docker run -d -p 8000:8000 myapp

