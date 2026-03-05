from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Basic configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mileage_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Blueprints for routes (example)
from routes import main_routes  # assuming you have a routes.py file

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)