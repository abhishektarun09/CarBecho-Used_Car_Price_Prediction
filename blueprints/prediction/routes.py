from src.utils import apology, login_required
from flask import render_template, request, Blueprint, jsonify

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from babel.numbers import format_currency


prediction_bp = Blueprint("prediction_bp", __name__, template_folder ="templates", static_folder="static")


@prediction_bp.route('/prediction', methods = ['GET','POST'])
@login_required
def predict():
    if request.method == 'GET':
        return render_template('prediction.html')
    else:
        if not request.form.get('km_driven'):
            return apology("Please enter Kilometers Driven", 400)
        if not request.form.get('fuel'):
            return apology("Please enter Fuel Type", 400)
        if not request.form.get('seller_type'):
            return apology("Please enter Seller Type", 400)
        if not request.form.get('transmission'):
            return apology("Please enter Transmission Type", 400)
        if not request.form.get('owner'):
            return apology("Please enter Owner Type", 400)
        if not request.form.get('mileage'):
            return apology("Please enter Mileage", 400)
        if not request.form.get('engine'):
            return apology("Please enter Engine CC", 400)
        if not request.form.get('max_power'):
            return apology("Please enter Max Power", 400)
        if not request.form.get('seats'):
            return apology("Please enter Number of Seats", 400)
        if not request.form.get('age'):
            return apology("Please enter Age of the Car", 400)
        
        data = CustomData(
            km_driven=request.form.get('km_driven'),
            fuel=request.form.get('fuel'),
            seller_type=request.form.get('seller_type'),
            transmission=request.form.get('transmission'),
            owner=request.form.get('owner'),
            mileage=request.form.get('mileage'),
            engine=request.form.get('engine'),
            max_power=request.form.get('max_power'),
            seats=request.form.get('seats'),
            age=request.form.get('age')
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()        
        results = predict_pipeline.predict(pred_df)
        
        formatted_prediction = format_currency(results[0], 'INR', locale='en_IN')
        return jsonify({"prediction": formatted_prediction})