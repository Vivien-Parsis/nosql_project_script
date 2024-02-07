from req_class import mongo_req
import time
start = time.time()

# Affiche sur l’ensemble du covid en France, le pourcentage de réanimations dans les hospitalisés.
aggregate = [
  {
    "$match": {
      "nom": "France",
    },
  },
  {
    "$group": {
      "_id": "France",
      "totalReanimation": {
        "$sum": "$reanimation",
      },
      "totalHospitalisation": {
        "$sum": "$hospitalises",
      },
      "totalGueris": {
        "$sum": "$gueris",
      },
    },
  },
  {
    "$project": {
      "_id": 0,
      "pays": "$_id",
      "PartDeRea": {
        "$round": [
          {
            "$divide": [
              "$totalHospitalisation",
              "$totalReanimation",
            ],
          },
          2,
        ],
      },
      "totalDeReanimation": "$totalReanimation",
      "totalDeHospitalisation": "$totalHospitalisation",
    },
  },
]

filePath = "./requests/req7_output.json"

find, findProject = {},{}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputAggregate()
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)