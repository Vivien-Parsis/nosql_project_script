import json
import pymongo

class mongo_req:
    
    def __init__(self, aggregate, filePath, findMatch, findProject):
        self.aggregate = aggregate
        self.filePath = filePath
        self.findMatch = findMatch
        self.findProject = findProject

    def getOutputAggregate(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nosql_project"]
        col = db["covid"]
        data = col.aggregate(self.aggregate)
        data_string = "["
        for item in data:
            data_string+=json.dumps(item)+",\n"
        data_string+="]"
        data_string = data_string.replace(",\n]","]")
        with open(self.filePath, "w") as file:
            file.write(data_string)
        client.close()

    def getOutputFind(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nosql_project"]
        col = db["covid"]
        data_string = "["
        data = col.find(self.findMatch,self.findProject)
        for item in data:
            data_string+=json.dumps(item)+",\n"
        data_string+="]"
        data_string = data_string.replace(",\n]","]")
        with open(self.filePath, "w") as file:
            file.write(data_string)
        client.close()