from pymongo import MongoClient

# Cria um bando de dados 
url = "mongodb://admin:th%40les789@localhost:27017/?authSource=admin"
client = MongoClient(url)

database = client["crud"] # cria um database 
col = database["users"] # cria um collection

