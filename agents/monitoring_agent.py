from mesa import Agent

class MonitoringAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Monitor system performance, such as data distribution
        for node in self.model.nodes:
            count = node.count_documents({})
            print(f"Node {node.name} contains {count} documents.")
