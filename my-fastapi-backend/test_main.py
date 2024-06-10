from fastapi.testclient import TestClient
from main import app
import requests

client = TestClient(app)

def test_read_cryptos_success():
    response = client.get("/cryptos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    assert "current_price" in response.json()[0]

def test_read_cryptos_failure():
    # Simulate a failed external API request
    original_get = requests.get

    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                raise requests.RequestException("Mocked request exception")
        return MockResponse()

    requests.get = mock_get
    response = client.get("/cryptos")
    assert response.status_code == 502
    assert response.json() == {"detail": "External API request failed"}

    # Restore original function
    requests.get = original_get

def test_read_cryptos_corrupted_data():
    # Simulate corrupted data
    original_get = requests.get

    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return [{"name": "Bitcoin"}]  # Missing 'current_price'
        return MockResponse()

    requests.get = mock_get
    response = client.get("/cryptos")
    assert response.status_code == 500
    assert response.json() == {"detail": "Corrupted or incomplete data received"}

    # Restore original function
    requests.get = original_get
