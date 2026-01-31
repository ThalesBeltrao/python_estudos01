from pymongo import MongoClient


url = "mongodb://admin:th%40les789@localhost:27017/?authSource=admin"
client = MongoClient(url)

print(client.list_database_names())


