from mesa import Agent
import time


class MonitoringAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Monitor system performance, such as data distribution
        for node in self.model.nodes:
            count = node.count_documents({})
            print(f"Node {node.name} contains {count} documents.")

            # Store node utilization metrics in MongoDB
            node_metrics = {
                "node_name": node.name,
                "data_count": count,
                "timestamp": time.time()
            }
            self.model.metrics_collection.insert_one(node_metrics)
