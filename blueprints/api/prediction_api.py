from flask import request, Blueprint, jsonify
from babel.numbers import format_currency

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.schemas.prediction_schema import PredictionRequestSchema

prediction_api = Blueprint("prediction_api", __name__)

@prediction_api.route('/api/v1/predict', methods=['POST'])
def predict_api():
    if not request.is_json:
        return jsonify({
            "success" : False,
            "error": "Request must be in JSON format"
        }), 415
        
    data = request.get_json()
            
    try:
        payload = PredictionRequestSchema(**data)
        custom_data = CustomData(
            km_driven=payload.km_driven,
            fuel=payload.fuel,
            seller_type=payload.seller_type,
            transmission=payload.transmission,
            owner=payload.owner,
            mileage=payload.mileage,
            engine=payload.engine,
            max_power=payload.max_power,
            seats=payload.seats,
            age=payload.age
        )
        pred_df = custom_data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()        
        results = predict_pipeline.predict(pred_df)

        
        formatted_prediction = format_currency(results[0], 'INR', locale='en_IN')
        
        return jsonify({
            "success": True,
            "formatted_prediction": formatted_prediction,
            "prediction" : results[0],
            "currency" : "INR"
        }), 200
        
    except Exception as e:
        return jsonify({
            "success" : False,
            "message" : "An error occurred during prediction",
            "error": str(e)
        }), 500