from mesa import Agent
import random
import time

class DataManagerAgent(Agent):
    def __init__(self, unique_id, model, db):
        super().__init__(unique_id, model)
        self.db = db

    def step(self):
        # Simulate some metrics (CPU, memory, network load) for demonstration
        cpu_usage = random.randint(10, 90)  # Placeholder for actual CPU usage
        memory_usage = random.randint(10, 90)  # Placeholder for actual memory usage
        network_load = random.randint(10, 90)  # Placeholder for actual network load

        # Simulate adding data to MongoDB
        data = {"key": self.unique_id, "value": f"Data managed by agent {self.unique_id}"}
        best_node = self.data_placement_decision(data)
        self.store_data(best_node, data)

        # Simulate storing metrics in MongoDB
        metrics_data = {
            "agent_id": self.unique_id,
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "network_load": network_load,
            "timestamp": time.time()
        }
        self.model.metrics_collection.insert_one(metrics_data)

    def data_placement_decision(self, data):
        # Placeholder logic for data placement, choosing a random node
        return self.random.choice(self.model.nodes)

    def store_data(self, node, data):
        node.insert_one(data)
