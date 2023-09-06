# Используйте базовый образ Python версии latest
FROM python:3.11.4

# Создайте директорию внутри контейнера, где будет размещено приложение
WORKDIR /app

# Скопируйте файлы вашего приложения в контейнер
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY credentials.json /app/credentials.json
COPY logo.jpg /app/logo.jpg

# Установите зависимости вашего приложения
RUN pip install -r requirements.txt

# Укажите команду, которая будет запускать ваше приложение внутри контейнера
CMD ["streamlit", "run", "./app.py", "[ARGUMENTS]"]
