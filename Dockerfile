FROM python:3.9

RUN apt-get update && apt-get install -y \
libpq-dev \
gcc \
&& rm -rf /var/lib/apt/lists/*

RUN pip install flask psycopg2-binary

WORKDIR /app
COPY . /app
CMD ["python", "app.py"]
EXPOSE 8080
