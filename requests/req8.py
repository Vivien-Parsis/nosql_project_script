from query_handler import mongodb_query_handler
import time
start = time.time()

# Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France
aggregate = [
  {
    "$facet": {
      "nombreDeJours": [
        {"$group": {"_id": "$date"}},
        {"$count": "nombre de jours"},
      ],
      "debut": [
        {"$group": {"_id": "$date"}},
        {"$sort": {"_id": 1}},
        {"$limit": 1}
      ],
      "fin": [
        {"$group": {"_id": "$date"}},
        {"$sort": {"_id": -1}},
        {"$limit": 1}
      ]
    }
  },
  {
    "$project": {
      "nombre de jours": {
        "$getField": {
          "field": "nombre de jours",
          "input": {"$first": "$nombreDeJours"}
        }
      },
      "debut": {
        "$getField": {
          "field": "_id",
          "input": {"$first": "$debut"}
        }
      },
      "fin": {
        "$getField": {
          "field": "_id",
          "input": {"$first": "$fin"}
        }
      }
    }
  }
]


filePath = "./requests/req8_output.json"

find, findProject = {},{}
description = "Requete pour afficher le total cumule du nombre de cas confirmes, de deces, et de personnes gueries en France"
req = mongodb_query_handler(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print(description)
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)