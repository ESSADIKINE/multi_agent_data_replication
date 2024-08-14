import unittest
from model.data_replication_model import DataReplicationModel

class TestDataReplicationModel(unittest.TestCase):

    def test_model_initialization(self):
        model = DataReplicationModel(num_agents=6)
        self.assertEqual(len(model.schedule.agents), 6)

if __name__ == "__main__":
    unittest.main()
