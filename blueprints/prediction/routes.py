from src.utils import login_required
from flask import render_template, Blueprint

prediction_bp = Blueprint("prediction_bp", __name__, template_folder ="templates", static_folder="static")

@prediction_bp.route('/prediction', methods = ['GET'])
@login_required
def predict():
    return render_template('prediction.html')