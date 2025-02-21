FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
libpq-dev \
gcc \
&& rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . /app
RUN pip install flask psycopg2
EXPOSE 8080
CMD ["python", "app.py"]
