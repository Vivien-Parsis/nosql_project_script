from req_class import mongo_req

# Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France
aggregate = [
  {
    "$facet": {
      "nombreDeJours": [
        {
          "$group": {
            "_id": "$date",
          },
        },
        {
          "$count": "nombre de jours",
        },
      ],
      "debut": [
        {
          "$group": {
            "_id": "$date",
          },
        },
        {
          "$sort": {
            "_id": 1,
          },
        },
        {
          "$limit": 1,
        },
      ],
      "fin": [
        {
          "$group": {
            "_id": "$date",
          },
        },
        {
          "$sort": {
            "_id": -1,
          },
        },
        {
          "$limit": 1,
        },
      ],
    },
  },
  {
    "$project": {
      "nombre de jours": {
        "$getField": {
          "field": "nombre de jours",
          input: {
            "$first": "$nombreDeJours",
          },
        },
      },
      "debut": {
        "$getField": {
          "field": "_id",
          "input": {
            "$first": "$debut",
          },
        },
      },
      "fin": {
        "$getField": {
          "field": "_id",
          "input": {
            "$first": "$fin",
          },
        },
      },
    },
  },
]

filePath = "./requests/req8_output.json"

find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()