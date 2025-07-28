from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib, json, sqlite3, datetime

app = Flask(__name__)
CORS(app)
conn = sqlite3.connect('sums.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS requests
    (id INTEGER PRIMARY KEY, numbers_hash TEXT, numbers_json TEXT, result_sum INTEGER, created_at TEXT)''')

def hash_numbers(numbers):
    return hashlib.sha256(json.dumps(sorted(numbers)).encode()).hexdigest()
@app.route('/')
def home():
    return "✅ Welcome to the Number Sum API! Use POST /sum with JSON: {\"numbers\": [1,2,3]}"

@app.route('/sum', methods=['POST'])
def compute_sum():
    data = request.get_json()
    numbers = data.get('numbers')

    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'Invalid input'}), 400

    h = hash_numbers(numbers)
    cursor.execute("SELECT result_sum FROM requests WHERE numbers_hash=?", (h,))
    row = cursor.fetchone()

    if row:
        return jsonify({'sum': row[0], 'cached': True})

    total = sum(numbers)
    cursor.execute("INSERT INTO requests (numbers_hash, numbers_json, result_sum, created_at) VALUES (?, ?, ?, ?)",
                   (h, json.dumps(numbers), total, datetime.datetime.now().isoformat()))
    conn.commit()
    return jsonify({'sum': total, 'cached': False})

if __name__ == '__main__':
    app.run(debug=True)
