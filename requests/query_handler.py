import json
import pymongo

class mongodb_query_handler:
    
    def __init__(self, aggregate=[], filePath="", findMatch={}, findProject={}):
        self.aggregate = aggregate
        self.filePath = filePath
        self.findMatch = findMatch
        self.findProject = findProject

    def getOutputAggregate(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nosql_project"]
        col = db["covid"]
        data_cursor, data_string, data_output = col.aggregate(self.aggregate), '[', []
        for item in data_cursor:
            data_output.append(item)
            data_string+=json.dumps(item)+",\n"
        data_string+="]"
        data_string = data_string.replace(",\n]","]")
        with open(self.filePath, "w") as file:
            file.write(data_string)
        client.close()
        return data_output

    def getOutputFind(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nosql_project"]
        col = db["covid"]
        data_cursor, data_string, data_output = col.find(self.findMatch,self.findProject), '[', []
        for item in data_cursor:
            data_output.append(item)
            data_string+=json.dumps(item)+",\n"
        data_string+="]"
        data_string = data_string.replace(",\n]","]")
        with open(self.filePath, "w") as file:
            file.write(data_string)
        client.close()
        return data_output