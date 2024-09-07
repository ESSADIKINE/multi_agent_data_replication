import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import psutil  # Importing psutil for system metrics
from flask import Flask, render_template, jsonify, redirect, url_for
from model.data_replication_model import DataReplicationModel
from pymongo import MongoClient

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
    print("Starting simulation...")

    for step in range(3):
        print(f"Running step {step + 1}")
        model.step()

    print("Simulation complete, redirecting...")
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
    return render_template('dashboard.html')  # Assuming you have a 'dashboard.html' file

@app.route('/data_distribution')
def data_distribution():
    # Example of real data distribution logic here (replace with your logic)
    data = {
        "node1": 120,
        "node2": 90,
        "node3": 150
    }
    return jsonify(data)

# Simulated data for Replication Details
@app.route('/replication_details')
def replication_details():
    # Simulate replication details (replace with your logic)
    data = {
        "node1": 15,  # Number of replicas for Node 1
        "node2": 12,  # Number of replicas for Node 2
        "node3": 20   # Number of replicas for Node 3
    }
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
