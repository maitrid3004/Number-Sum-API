import requests

def test_sum_success():
    r = requests.post("http://localhost:5000/sum", json={"numbers": [10, 20]})
    assert r.status_code == 200
    assert r.json()['sum'] == 30

def test_invalid_input():
    r = requests.post("http://localhost:5000/sum", json={"numbers": ["x", 20]})
    assert r.status_code == 400
