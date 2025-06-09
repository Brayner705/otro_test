FROM python:3.12.4

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 8000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]