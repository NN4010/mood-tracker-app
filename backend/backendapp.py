from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
@app.route('/')
def home():
    return "Mood Tracker Backend is Running!"
CORS(app)

# Initialize database
def init_db():
    conn = sqlite3.connect('moods.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY,
            mood TEXT,
            note TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/save_mood', methods=['POST'])
def save_mood():
    data = request.json
    mood = data.get('mood')
    note = data.get('note')
    date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect('moods.db')
    c = conn.cursor()
    c.execute('INSERT INTO moods (mood, note, date) VALUES (?, ?, ?)', (mood, note, date))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Mood saved successfully!'})

@app.route('/get_moods', methods=['GET'])
def get_moods():
    conn = sqlite3.connect('moods.db')
    c = conn.cursor()
    c.execute('SELECT mood, note, date FROM moods ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()

    moods = [{'mood': row[0], 'note': row[1], 'date': row[2]} for row in rows]
    return jsonify({'moods': moods})

if __name__ == '__main__':
    app.run(debug=True)

