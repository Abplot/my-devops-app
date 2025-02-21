from flask import Flask, request 
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="172.17.0.1",
        database="devops_app",
        user="postgres",
        password="password123"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    conn.close()
    return f"Connected to PostgreSQL! Database version: {db_version[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
