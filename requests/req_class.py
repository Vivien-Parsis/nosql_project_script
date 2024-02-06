import json
import pymongo

class mongo_req:
    
    def __init__(self, aggregate, filePath, find, findProject):
        self.aggregate = aggregate
        self.filePath = filePath
        self.find = find
        self.findProject = findProject
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nosql_project"]
        self.col = self.db["covid"]

    def getOutputAggregate(self):
        data = self.col.aggregate(self.aggregate)
        data_string = "["
        for item in data:
            data_string+=json.dumps(item)+",\n"
        data_string+="]"
        data_string = data_string.replace(",\n]","]")
        with open(self.filePath, "w") as file:
            file.write(data_string)
    def getOutputFind(self):
        data = self.col.find(self.find, self.findProject)
        # with open(self.filePath, "w") as file:
        #     file.write(data)