from query_handler import mongodb_query_handler
import time
start = time.time()
# Affiche le nombre hospitalisation total par département
aggregate =[
  {"$match": {"code": {"$regex":"DEP-.*"}}},
  {
    "$group": {
      "_id": "$nom",
     " toalHospitalises": {"$sum": "$hospitalises"},
    }
  },
  {"$sort": {"toalHospitalises": -1}},
  {"$project": {"departement": "$_id","_id": 0,"toalHospitalises": 1}}
]


filePath = "./requests/req4_output.json"

find, findProject = {},{}
description = "Affiche le nombre hospitalisation total par departement"
req = mongodb_query_handler(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print(description)
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)