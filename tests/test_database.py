import unittest
from database.db_connection import MongoDBConnection

class TestDatabaseConnection(unittest.TestCase):

    def test_connection(self):
        db_conn = MongoDBConnection()
        db = db_conn.get_database("test_db")
        self.assertIsNotNone(db)

if __name__ == "__main__":
    unittest.main()
