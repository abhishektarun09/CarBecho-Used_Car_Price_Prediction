import os

from flask import Flask
from flask_session import Session
from flask_wtf import CSRFProtect

from blueprints.account_management.routes import accounts_bp
from blueprints.account_management.change_password import change_password_bp
from blueprints.prediction.routes import prediction_bp
from blueprints.index.routes import index_bp
from blueprints.api.prediction_api import prediction_api

from src.config import Config
from database import db

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Session(app)
csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()
    
app.register_blueprint(index_bp)

app.register_blueprint(accounts_bp)

app.register_blueprint(change_password_bp)

app.register_blueprint(prediction_bp)

csrf.exempt(prediction_api)
app.register_blueprint(prediction_api)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
