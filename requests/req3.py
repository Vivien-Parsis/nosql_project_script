from req_class import mongo_req

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
filePath = "./requests/req3_output.json"

find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()