from flask import Blueprint, request, jsonify, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/upload-mileage', methods=['GET', 'POST'])
def upload_mileage():
    if request.method == 'GET':
        return render_template('upload_mileage.html')
    return jsonify({'message': 'Mileage photo uploaded successfully!'}), 201

@main_routes.route('/view-reports', methods=['GET'])
def view_reports():
    return render_template('records.html')

@main_routes.route('/add-fuel-record', methods=['GET', 'POST'])
def add_fuel_record():
    if request.method == 'GET':
        return render_template('add_fuel.html')
    return jsonify({'message': 'Fuel fill record added successfully!'}), 201

@main_routes.route('/monthly-fuel-expense', methods=['GET'])
def display_monthly_fuel_expense():
    return render_template('monthly_report.html')