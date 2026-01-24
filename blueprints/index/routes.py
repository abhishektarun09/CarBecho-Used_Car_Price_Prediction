from flask import render_template, Blueprint

from datetime import datetime

index_bp = Blueprint("index_bp", __name__, template_folder ="templates", static_folder="static")


@index_bp.route('/')
def index():
    return render_template('index.html', current_year = datetime.now().year) 