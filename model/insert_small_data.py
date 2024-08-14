from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db1 = client["node1_db"]["data"]
db2 = client["node2_db"]["data"]
db3 = client["node3_db"]["data"]

# Small dataset to insert into the database
small_dataset = [
    {"key": 1, "value": "data1"},
    {"key": 2, "value": "data2"},
    {"key": 3, "value": "data3"},
]

# Clear existing data (optional)
db1.delete_many({})
db2.delete_many({})
db3.delete_many({})

# Insert the small dataset into one of the nodes
db1.insert_many(small_dataset)

print("Small dataset inserted successfully.")
