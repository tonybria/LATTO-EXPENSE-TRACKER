from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure your database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)
