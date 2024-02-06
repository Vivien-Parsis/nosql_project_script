from req_class import mongo_req
import time
start = time.time()
# Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France
aggregate = [
  {
    "$match": {
      "nom": "France",
    },
  },
  {
    "$group": {
      "_id": "France",
      "totalCasConfirme": {
        "$sum": "$casConfirmes",
      },
      "totalDeces": {
        "$sum": "$deces",
      },
      "totalGueris": {
        "$sum": "$gueris",
      },
    },
  },
  {
    "$project": {
      "pays": "$_id",
      "_id": 0,
      "totalCasConfirme": 1,
      "totalDeces": 1,
      "totalGueris": 1,
    },
  },
]
filePath = "./requests/req1_output.json"
find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)