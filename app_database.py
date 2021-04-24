import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["event"]

def insert_data(data):
    mycol.insert_one(data)
    for x in mycol.find():
        print(x)
 