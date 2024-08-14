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
        self.nodes = [self.db1, self.db2, self.db3]

        # Create agents
        for i in range(self.num_agents):
            if i < 2:
                agent = DataManagerAgent(i, self, self.nodes[i % len(self.nodes)])
            elif i < 4:
                agent = ReplicationAgent(i, self)
            else:
                agent = MonitoringAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()
