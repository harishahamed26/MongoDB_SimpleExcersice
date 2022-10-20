import pymongo
from pymongo import *
import pandas as pd
import json


#Checking whether the connection 

try:
    Connection = MongoClient("mongodb+srv://harry:<pass>@cluster0.bgi3n46.mongodb.net/?retryWrites=true&w=majority")
    #client = pymongo.MongoClient(connect=True, serverSelectionTimeoutMS=5000)
    print("Connected to the Server")
    #print(client.server_info())
except Exception:
    print( "Connection to the Server is unsuccessful")

# Reading the CSV file and converting it into Json File
myTestingCSVData  = pd.read_csv("/Users/harishahamed26gmail.com/Documents/Python files/lab7/mongoDB_testingFile.csv")
#print(myTestingCSVData.head(10))
myTestingCSVData.to_json("/Users/harishahamed26gmail.com/Documents/Python files/lab7/mongoDB_testingFile.json")
myTestingJSonData = open("/Users/harishahamed26gmail.com/Documents/Python files/lab7/mongoDB_testingFile.json")
jsonData          = json.load(myTestingJSonData)

# inserting the Json data to the mongoDB
DB  = Connection["Lab7_DB"]
Col = DB["Testing_Collection"]
Col.insert_many([jsonData])
print("Json Data Inserted")

# Dropping the Created Collection
#Col.drop()
print(f'The collection {Col} is dropped sucessfully')

col_list = DB.list_collection_names()
for i in col_list:
    print(i)
