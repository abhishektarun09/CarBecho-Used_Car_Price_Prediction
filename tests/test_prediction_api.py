# tests/conftest.py
import pytest
from flask import Flask
from blueprints.api.prediction_api import prediction_api

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(prediction_api)
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# tests/test_prediction_api.py
def test_predict_api_success(client, mocker):
    # Mock PredictPipeline.predict
    mock_predict = mocker.patch(
        "src.pipeline.predict_pipeline.PredictPipeline.predict",
        return_value=[450000.0]
    )

    payload = {
        "km_driven": 50000,
        "fuel": "Diesel",
        "seller_type": "Dealer",
        "transmission": "Manual",
        "owner": "First Owner",
        "mileage": 20.0,
        "engine": 1248,
        "max_power": 74.0,
        "seats": 5,
        "age": 5
    }

    response = client.post(
        "/api/v1/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.get_json()
    assert data["success"] is True
    assert data["prediction"] == 450000.0
    assert data["currency"] == "INR"
    assert "formatted_prediction" in data

    mock_predict.assert_called_once()

def test_predict_api_non_json_request(client):
    response = client.post(
        "/api/v1/predict",
        data="not json",
        content_type="text/plain"
    )

    assert response.status_code == 415

    data = response.get_json()
    assert data["success"] is False
    assert data["error"] == "Request must be in JSON format"

def test_predict_api_exception(client, mocker):
    # Force PredictPipeline to raise an exception
    mocker.patch(
        "src.pipeline.predict_pipeline.PredictPipeline.predict",
        side_effect=Exception("Model failure")
    )

    payload = {
        "km_driven": 50000,
        "fuel": "Diesel",
        "seller_type": "Dealer",
        "transmission": "Manual",
        "owner": "First Owner",
        "mileage": 20.0,
        "engine": 1248,
        "max_power": 74.0,
        "seats": 5,
        "age": 5
    }

    response = client.post("/api/v1/predict", json=payload)

    assert response.status_code == 500

    data = response.get_json()
    assert data["success"] is False
    assert data["message"] == "An error occurred during prediction"

