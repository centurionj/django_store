FROM python:3.11

# Переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Рабочая директория
WORKDIR /app

# Зависимости Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установка nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean

# Копирование исходного кода Django приложения в образ
COPY . /app/

# Копирование конфигурации Nginx
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Экспорт порта, на котором работает приложение
EXPOSE 8000

# Запуск команды для старта Django, Celery и Nginx
CMD sh -c "python /app/manage.py migrate && \
          python /app/manage.py collectstatic --noinput && \
          gunicorn shop.wsgi:application --bind 0.0.0.0:8000 & \
          celery -A shop worker -l info & \
          nginx -g 'daemon off;'"
