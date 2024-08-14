import unittest
from agents.data_manager_agent import DataManagerAgent
from agents.replication_agent import ReplicationAgent
from agents.monitoring_agent import MonitoringAgent

class TestAgents(unittest.TestCase):

    def test_data_manager_agent(self):
        agent = DataManagerAgent(1, None, None)
        self.assertEqual(agent.unique_id, 1)

    def test_replication_agent(self):
        agent = ReplicationAgent(2, None)
        self.assertEqual(agent.unique_id, 2)

    def test_monitoring_agent(self):
        agent = MonitoringAgent(3, None)
        self.assertEqual(agent.unique_id, 3)

if __name__ == "__main__":
    unittest.main()
