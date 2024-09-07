# Filename: data_replication_model.py

from mesa import Model
from mesa.time import RandomActivation
from pymongo import MongoClient
from agents.data_manager_agent import DataManagerAgent
from agents.replication_agent import ReplicationAgent
from agents.monitoring_agent import MonitoringAgent

class DataReplicationModel(Model):
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)

        # Set up MongoDB connections (simulating nodes)
        self.client = MongoClient('localhost', 27017)
        self.db1 = self.client["node1_db"]["data"]
        self.db2 = self.client["node2_db"]["data"]
        self.db3 = self.client["node3_db"]["data"]
        self.metrics_collection = self.client["metrics_db"]["metrics"]
        self.nodes = [self.db1, self.db2, self.db3]

        # Initialize dictionaries to track data distribution and replication details
        self.data_distribution = {"node1": 0, "node2": 0, "node3": 0}
        self.replication_details = {"node1": 0, "node2": 0, "node3": 0}

        # Create agents
        for i in range(self.num_agents):
            if i < 2:
                agent = DataManagerAgent(i, self, self.nodes[i % len(self.nodes)])
            elif i < 4:
                agent = ReplicationAgent(i, self)
            else:
                agent = MonitoringAgent(i, self)
            self.schedule.add(agent)

    def update_data_distribution(self):
        # Update data distribution based on document counts in each node
        self.data_distribution = {
            "node1": self.db1.count_documents({}),
            "node2": self.db2.count_documents({}),
            "node3": self.db3.count_documents({})
        }

    def update_replication_details(self):
        # Example logic for tracking replicated data
        self.replication_details = {
            "node1": self.db1.count_documents({"replicated": True}),
            "node2": self.db2.count_documents({"replicated": True}),
            "node3": self.db3.count_documents({"replicated": True})
        }

    def step(self):
        # Execute a step in the simulation for all agents
        self.schedule.step()

        # After each step, update the data distribution and replication details
        self.update_data_distribution()
        self.update_replication_details()

        # Optionally, store the metrics in the MongoDB metrics collection
        metrics_data = {
            "data_distribution": self.data_distribution,
            "replication_details": self.replication_details
        }
        self.metrics_collection.insert_one(metrics_data)
