import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    
    # Database Settings
    _user = os.getenv("MYSQL_USER")
    _pw = os.getenv("MYSQL_PASSWORD")
    _host = os.getenv("MYSQL_HOST")
    _port = os.getenv("MYSQL_PORT")
    _db = os.getenv("MYSQL_DB")
    
    # SSL Path Setup
    _base_dir = os.path.dirname(os.path.abspath(__file__))
    _ssl_ca_path = os.path.join(_base_dir, "cert", "DigiCertGlobalRootCA.crt.pem")
    
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{_user}:{_pw}@{_host}:{_port}/{_db}"
        #f"?ssl_ca={_ssl_ca_path}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False