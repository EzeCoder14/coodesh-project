from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_salesforce_success():
    response = client.post(
        "/integrate/salesforce",
        json={"action": "created_lead", "parameters": {"name": "John"}},
        headers={"Authorization": "Bearer dummy_token"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["provider"] == "salesforce"