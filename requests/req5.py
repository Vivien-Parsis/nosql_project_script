from req_class import mongo_req
import time
start = time.time()

# Affiche le nombre de décès et de guéris totaux par régions
aggregate = [
  {
    "$match": {
      "code": {"$regex":"REG-.*"},
    },
  },
  {
    "$group": {
      "_id": "$nom",
      "deces": {
        "$sum": "$deces",
      },
      "gueris": {
        "$sum": "$gueris",
      },
    },
  },
  {
    "$project": {
      "_id": 0,
      "region": "$_id",
      "deces": 1,
      "gueris": 1,
    },
  },
  {
    "$sort": {
      "region": 1,
    },
  },
]

filePath = "./requests/req5_output.json"

find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)