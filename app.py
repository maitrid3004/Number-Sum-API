from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import hashlib
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sum_cache.db'
db = SQLAlchemy(app)

class SumCache(db.Model):
    id = db.Column(db.String, primary_key=True)
    input = db.Column(db.Text, unique=True, nullable=False)
    result = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    numbers = data.get('numbers', [])

    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'Invalid input'}), 400

    key = hashlib.md5(json.dumps(numbers).encode()).hexdigest()
    cached = SumCache.query.get(key)

    if cached:
        return jsonify({'sum': cached.result, 'cached': True})

    result = sum(numbers)
    new_entry = SumCache(id=key, input=json.dumps(numbers), result=result)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'sum': result, 'cached': False})

if __name__ == '__main__':
    app.run(debug=True)
