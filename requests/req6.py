from req_class import mongo_req
import time
start = time.time()

# Affiche le département avec le moins et le plus de décès de covid
aggregate = [
  {
    "$facet": {
      "minVal": [
        {
          "$match": {
            "code": {"$regex":"DEP-.*"},
          },
        },
        {
          "$group": {
            "_id": "$nom",
            "deces": {
              "$sum": "$deces",
            },
          },
        },
        {
          "$sort": {
            "deces": 1,
          },
        },
        {
          "$limit": 1,
        },
        {
          "$project": {
            "departement": "$_id",
            "_id": 0,
            "deces": 1,
          },
        },
      ],
      "maxVal": [
        {
          "$match": {
            "code": {"$regex":"DEP-.*"},
          },
        },
        {
          "$group": {
            "_id": "$nom",
            "deces": {
              "$sum": "$deces",
            },
          },
        },
        {
          "$sort": {
            "deces": -1,
          },
        },
        {
          "$limit": 1,
        },
        {
          "$project": {
            "departement": "$_id",
            "_id": 0,
            "deces": 1,
          },
        },
      ],
    },
  },
  {
    "$project": {
      "min": {
        "$first": "$minVal",
      },
      "max": {
        "$first": "$maxVal",
      },
    },
  },
]

filePath = "./requests/req6_output.json"

find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)