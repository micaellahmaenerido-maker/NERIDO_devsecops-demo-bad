import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_discount_calculation(client):
    # Testing a $50 item. A 10% discount should result in $45.
    response = client.get('/api/discount?price=50')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["original_price"] == 50.0
    # This assertion will fail because the buggy code returns 40.0
    assert data["discounted_price"] == 45.0