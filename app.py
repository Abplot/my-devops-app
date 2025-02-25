from flask import Flask, render_template, request, redirect
import psycopg2
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="devops_app",
        user="devops_user",
        password="password123",
        port="5432"
    )
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        message = request.form['message']
        cursor.execute('INSERT INTO messages (content) VALUES (%s)', (message,))
        conn.commit()
        return redirect('/')
    
    cursor.execute('SELECT * FROM messages ORDER BY created_at DESC')
    messages = cursor.fetchall()
    conn.close()
    
    # Преобразуем в список словарей для удобства в шаблоне
    messages_list = [{
        'content': msg[1],
        'created_at': msg[2]
    } for msg in messages]
    
    return render_template('index.html', messages=messages_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
