import matplotlib.pyplot as plt
import numpy as np
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nosql_project"]
col = db["covid"]

query = [
  {"$match":{"nom":"Île-de-France"}},
  {
    "$group": {
      "_id": "$date",
      "hospitalises": {"$sum": "$hospitalises"},
      "reanimation": {"$sum": "$reanimation"},
      "nouvellesHospitalisations":{"$sum": "$nouvellesHospitalisations"},
  	}
  },
  {"$sort":{"_id":1}},
  {
    "$project" : {
     "_id" : 0,
      "date" : "$_id",
      "hospitalises":1,
      "nouvellesHospitalisations":1,
      "reanimation":1
    }
  }
]

data = col.aggregate(query)
date, hospitalises, nouvellesHospitalisations, reanimation = [],[],[],[]
hour = " 00:00:00"
for plot in data:
    reanimation.append(plot["reanimation"])
    currentDate = datetime.strptime(plot["date"]+hour, '%Y-%m-%d %H:%M:%S')
    currentTimeStamp = currentDate.timestamp()
    date.append(currentTimeStamp)
    hospitalises.append(plot["hospitalises"])
    nouvellesHospitalisations.append(plot["nouvellesHospitalisations"])

plt.style.use('_mpl-gallery')
plt.plot(date,hospitalises,color="blue")
plt.plot(date,nouvellesHospitalisations,color="red")
plt.plot(date,reanimation,color="green")
plt.show()