from query_handler import mongodb_query_handler
import time
start = time.time()

# Affiche le nombre de décès et de guéris totaux par régions
aggregate = [
  {"$match": {"code": {"$regex":"REG-.*"}}},
  {
    "$group": {
      "_id": "$nom",
      "deces": {"$sum": "$deces"},
      "gueris": {"$sum": "$gueris"}
    }
  },
  {"$project": {"_id":0,"region":"$_id","deces":1,"gueris":1}},
  {"$sort": {"region": 1}}
]


filePath = "./requests/req5_output.json"

find, findProject = {},{}
description = "Affiche le nombre de decees et de gueris totaux par regions"
req = mongodb_query_handler(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print(description)
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)