from mesa import Agent

class ReplicationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Logic to replicate data across nodes
        for node in self.model.nodes:
            self.replicate_data(node)

    def replicate_data(self, node):
        # Fetch all documents from the node
        data = node.find()
        for doc in data:
            # Remove the '_id' field to avoid DuplicateKeyError
            doc.pop('_id', None)
            for other_node in self.model.nodes:
                if other_node != node:
                    try:
                        other_node.insert_one(doc)
                    except Exception as e:
                        print(f"Error replicating document: {e}")