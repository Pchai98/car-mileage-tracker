import sqlite3

# Connect to SQLite database
db_name = 'car_mileage_tracker.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS mileage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    date TEXT NOT NULL,
    miles INTEGER NOT NULL,
    FOREIGN KEY (car_id) REFERENCES cars (id)
)''')

# Initialize database with sample data
cars = [
    ('Toyota', 'Camry', 2020),
    ('Honda', 'Accord', 2021),
    ('Ford', 'Focus', 2019)
]

cursor.executemany('''INSERT INTO cars (make, model, year) VALUES (?, ?, ?)''', cars)

# Sample mileage data
mileage_data = [
    (1, '2026-03-01', 150),
    (1, '2026-03-02', 200),
    (2, '2026-03-03', 175)
]

cursor.executemany('''INSERT INTO mileage (car_id, date, miles) VALUES (?, ?, ?)''', mileage_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print('Database initialized with sample data.')