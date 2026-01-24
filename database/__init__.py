from flask_sqlalchemy import SQLAlchemy

# We don't pass 'app' here yet to avoid circular imports
db = SQLAlchemy()