import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import psutil
import time  # Import time to manage the 10-minute simulation
from flask import Flask, render_template, jsonify, redirect, url_for
from model.data_replication_model import DataReplicationModel
from pymongo import MongoClient

# Add the parent directory to sys.path so Python can find 'model'

app = Flask(__name__)

# Initialize model globally with fewer steps
model = DataReplicationModel(num_agents=6)

def delete_databases():
    client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB

    # List the names of your MongoDB databases
    databases_to_delete = ["node1_db", "node2_db", "node3_db"]

    # Drop the databases completely
    for db_name in databases_to_delete:
        if db_name in client.list_database_names():
            client.drop_database(db_name)
            print(f"Database {db_name} deleted.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_simulation')
def run_simulation():
    print("Starting 2-minute simulation...")  # Adjusted to 2-minute simulation

    start_time = time.time()  # Record the start time
    simulation_duration = 20  # 2 minutes in seconds (120 seconds)

    # Run the simulation for 2 minutes
    while time.time() - start_time < simulation_duration:
        model.step()  # Execute a step in the simulation
        
        time.sleep(1)  # Optional: Pause for 1 second between steps to reduce CPU usage

    print("2-minute simulation complete.")
    return redirect(url_for('distribution'))


@app.route('/distribution')
def distribution():
    # Connect to MongoDB nodes
    client = MongoClient('localhost', 27017)
    db1 = client["node1_db"]["data"]
    db2 = client["node2_db"]["data"]
    db3 = client["node3_db"]["data"]

    node1_count = db1.count_documents({})
    node2_count = db2.count_documents({})
    node3_count = db3.count_documents({})

    return render_template('distribution.html', node1=node1_count, node2=node2_count, node3=node3_count)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data_distribution')
def data_distribution():
    # Fetch the data distribution from the model
    data = model.data_distribution
    return jsonify(data)

@app.route('/replication_details')
def replication_details():
    # Fetch the replication details from the model
    data = model.data_distribution
    return jsonify(data)

# Real-time Performance Metrics using psutil
@app.route('/metrics')
def get_metrics():
    # Get real-time system metrics using psutil
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage in percentage
    memory_info = psutil.virtual_memory()  # Memory info
    net_io = psutil.net_io_counters()  # Network input/output statistics

    # Prepare the data to return as JSON
    metrics_data = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,  # Memory usage in percentage
        "network_sent": net_io.bytes_sent / (1024 * 1024),  # Convert to MB
        "network_received": net_io.bytes_recv / (1024 * 1024)  # Convert to MB
    }

    return jsonify(metrics_data)

if __name__ == "__main__":
    delete_databases()  # Delete the databases before starting the Flask app
    app.run(debug=True)
