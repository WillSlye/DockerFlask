from flask import Flask
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logs (endpoint TEXT)")
    conn.commit()
    conn.close()

@app.route('/microservice')
def microservice():
    # Log the microservice call to the database
    create_table()
    log_to_database('/microservice')

    return 'Microservice endpoint'

def log_to_database(endpoint):
    # Connect to the database
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()

    # Insert the endpoint into the logs table
    c.execute("INSERT INTO logs (endpoint) VALUES (?)", (endpoint,))
    conn.commit()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
