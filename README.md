# 🔢 Number Sum API

Welcome to the **Number Sum API** – a simple and efficient API that calculates the sum of numbers in a given list. Built with Python and Flask.

## ✅ How It Works

- **Endpoint:** `POST /sum`
- **Request Body:**

```json
{
  "numbers": [1, 2, 3, 4]
}
````

* **Response:**

```json
{
  "sum": 10,
  "cached": false
}
```

If you send the same list again, it will return:

```json
{
  "sum": 10,
  "cached": true
}
```

## 🚀 Features

* Calculates sum of an array of numbers.
* Uses a database to cache results and reduce recomputation.
* Returns if the result was retrieved from the cache.

## 🧪 How to Test

You can test the API using **Postman** or **curl**:

```bash
curl -X POST http://localhost:5000/sum \
-H "Content-Type: application/json" \
-d '{"numbers": [5, 10, 15]}'
```

## 🛠 Technologies Used

* Python 3
* Flask
* MongoDB (for caching)

## 📂 Project Structure

```
sum_api_project/
│
├── app.py         # Main Flask app
├── requirements.txt
└── README.md
```

## 📌 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/maitrid3004/Number-Sum-API.git
   cd Number-Sum-API
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask app:

   ```bash
   python app.py
   ```

   <img width="1698" height="823" alt="image" src="https://github.com/user-attachments/assets/5189fbd1-fe47-4623-89e6-d138e63acb63" />



