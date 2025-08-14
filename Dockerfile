# Use official Python image
FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "ioss_project.wsgi", "--bind", "0.0.0.0:8000"]
