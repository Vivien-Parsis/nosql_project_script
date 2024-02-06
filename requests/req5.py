from req_class import mongo_req

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