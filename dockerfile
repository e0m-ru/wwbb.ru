# Используем официальный Python образ
FROM python:latest

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем и переходим в рабочую директорию
WORKDIR /code

# Устанавливаем зависимости
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Ensure media and database are not overwritten
VOLUME ["/code/media", "/code/db.sqlite3"]

# Копируем проект
COPY . /code/

# Команда для запуска (может потребоваться изменить в зависимости от вашего проекта)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djsite.wsgi:application"]