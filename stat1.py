import matplotlib.pyplot as plt
import numpy as np
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nosql_project"]
col = db["covid"]

query = [
  {
    "$group": {
      "_id": "$date",
      "deces": {
        "$sum": "$deces",
      },
      "gueris": {
        "$sum": "$gueris",
      },
      "confirmes": {
        "$sum": "$casConfirmes",
      },
    },
  },
  {
    "$sort": {
      "_id": 1,
    },
  },
  {
    "$project": {
      "_id": 0,
      "date": "$_id",
      "deces": 1,
      "gueris": 1,
      "confirmes": 1,
    },
  },
]


data = col.aggregate(query)
date, confirmes, gueris, deces = [],[],[],[]
hour = " 00:00:00"
for plot in data:
    currentDate = datetime.strptime(plot["date"]+hour, '%Y-%m-%d %H:%M:%S')
    currentTimeStamp = currentDate.timestamp()
    date.append(currentTimeStamp)
    confirmes.append(plot["confirmes"])
    gueris.append(plot["gueris"])
    deces.append(plot["deces"])


plt.style.use('_mpl-gallery')
plt.plot(date,confirmes,color="green")
plt.plot(date,deces,color="red")
plt.plot(date,gueris,color="blue")
plt.show()