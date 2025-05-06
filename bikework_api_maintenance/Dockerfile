# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/requirements.txt

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expone el puerto 8000
EXPOSE 80

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "bikework_api_maintenance/manage.py", "runserver", "0.0.0.0:80"]