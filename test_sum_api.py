import requests

def test_sum_valid():
    res = requests.post("http://localhost:5000/sum", json={"numbers": [1, 2, 3]})
    assert res.status_code == 200
    assert res.json()["sum"] == 6

def test_sum_empty():
    res = requests.post("http://localhost:5000/sum", json={"numbers": []})
    assert res.status_code == 200
    assert res.json()["sum"] == 0

def test_sum_invalid_type():
    res = requests.post("http://localhost:5000/sum", json={"numbers": [1, "a", 3]})
    assert res.status_code == 400
