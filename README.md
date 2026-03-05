# Car Mileage Tracker

## Project Overview
The Car Mileage Tracker is a web application designed to help users track their vehicle's mileage and fuel consumption efficiently. By utilizing advanced image recognition technology, the application can read mileage information from photos and extract relevant metadata, allowing for accurate tracking of fuel expenses and consumption patterns.

## Features
- **Mileage Reading**: Capture mileage directly from photographs using OCR (Optical Character Recognition).
- **Metadata Extraction**: Obtain additional details such as date and time from the photographs.
- **Fuel Consumption Tracking**: Monitor fuel consumption against recorded mileage.
- **Monthly Reports**: Generate reports based on PTT fuel prices to analyze spending and fuel efficiency.
- **User-Friendly Interface**: Easy-to-use web application accessible on various devices.

## Installation
To get started with the Car Mileage Tracker, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Pchai98/car-mileage-tracker.git
   ```
2. Navigate into the directory:
   ```bash
   cd car-mileage-tracker
   ```
3. Install the necessary dependencies:
   ```bash
   npm install
   ```
4. Set up your environment variables as needed,
   ideally in a `.env` file.
5. Start the application:
   ```bash
   npm start
   ```

## Usage
- **Uploading Photos**: Use the application interface to upload photos of your vehicle's odometer.
- **View Logs**: Navigate to the "Logs" section to view all the recorded mileage and fuel consumption entries.
- **Generating Reports**: Access the "Reports" section to generate monthly reports based on the recorded data and current fuel prices.

## Architecture
The application is built using a modern web stack:
- **Frontend**: React.js for building dynamic user interfaces.
- **Backend**: Node.js with Express.js for server-side logic and API handling.
- **Database**: MongoDB for storing user data, mileage logs, and report information.
- **API**: RESTful API to facilitate communication between the frontend and backend.

## API Documentation
### Endpoints:
- **POST /api/mileage**: Upload mileage entry from a photo.
  - **Request Body**: { photo: <image_base64>, date: <date>, fuel_price: <price> }
  - **Response**: { success: boolean, message: string, data: <entry_data> }

- **GET /api/mileage**: Retrieve all mileage entries for a user.
  - **Response**: { success: boolean, data: [<entry_data>] }

- **GET /api/reports/monthly**: Generate a monthly report based on recorded entries and fuel prices.
  - **Response**: { success: boolean, report: <report_data> }

## Contribution
Contributions are welcome! Please create an issue or submit a pull request for any improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.