from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)
app.app_context().push()


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# blueprints - errors
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

# blueprints - table
from app.tables import tb as tables_bp
app.register_blueprint(tables_bp)

from app import routes, models


