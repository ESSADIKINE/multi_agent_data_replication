from mesa import Agent

class DataManagerAgent(Agent):
    def __init__(self, unique_id, model, db):
        super().__init__(unique_id, model)
        self.db = db

    def step(self):
        data = {"key": self.unique_id, "value": f"Data managed by agent {self.unique_id}"}
        best_node = self.data_placement_decision(data)
        self.store_data(best_node, data)

    def data_placement_decision(self, data):
        # Placeholder logic for data placement, choosing a random node
        return self.random.choice(self.model.nodes)

    def store_data(self, node, data):
        node.insert_one(data)
