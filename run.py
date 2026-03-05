from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from your_application import create_app

# Initialize Flask application
app = create_app()

# Initialize the database
with app.app_context():
    db = SQLAlchemy(app)
    db.create_all()  # Create database tables if they don't exist

if __name__ == '__main__':
    app.run(debug=True)