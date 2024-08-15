import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, redirect, url_for
from model.data_replication_model import DataReplicationModel
from pymongo import MongoClient

app = Flask(__name__)

# Initialize model globally with fewer steps
model = DataReplicationModel(num_agents=6)

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

if __name__ == "__main__":
    app.run(debug=True)
