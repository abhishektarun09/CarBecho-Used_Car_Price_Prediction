from flask import request, Blueprint, jsonify
from babel.numbers import format_currency

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


prediction_api = Blueprint("prediction_api", __name__)

REQUIRED_FIELDS = [
    "km_driven",
    "fuel",
    "seller_type",
    "transmission",
    "owner",
    "mileage",
    "engine",
    "max_power",
    "seats",
    "age"
]

@prediction_api.route('/api/v1/predict', methods=['POST'])
def predict_api():
    if not request.is_json:
        return jsonify({
            "success" : False,
            "error": "Request must be in JSON format"
        }), 415
        
    data = request.get_json()
    
    for field in REQUIRED_FIELDS:
        if field not in data:
            return jsonify({
                "success" : False,
                "error": f"Missing required field: {field}"
            }), 400
            
    try:
        custom_data = CustomData(
            km_driven=data['km_driven'],
            fuel=data['fuel'],
            seller_type=data['seller_type'],
            transmission=data['transmission'],
            owner=data['owner'],
            mileage=data['mileage'],
            engine=data['engine'],
            max_power=data['max_power'],
            seats=data['seats'],
            age=data['age']
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