import requests

def test_flask_app():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    assert response.text == "Hello from Jenkins Docker CI/CD Project!"
