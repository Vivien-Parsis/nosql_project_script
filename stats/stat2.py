import json
import matplotlib.pyplot as plt
import pymongo
from datetime import datetime
import time
start = time.time()

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
data_string = "["
date, hospitalises, nouvellesHospitalisations, reanimation = [],[],[],[]
hour = " 00:00:00"
for plot in data:
    data_string+=json.dumps(plot)+",\n"
    reanimation.append(plot["reanimation"])
    currentDate = datetime.strptime(plot["date"]+hour, '%Y-%m-%d %H:%M:%S')
    currentTimeStamp = currentDate.timestamp()
    date.append(currentTimeStamp)
    hospitalises.append(plot["hospitalises"])
    nouvellesHospitalisations.append(plot["nouvellesHospitalisations"])
data_string+="]"
data_string = data_string.replace(",\n]","]")
with open("./stats/stat2_output.json", "w") as file:
    file.write(data_string)

plt.style.use('_mpl-gallery')
plt.plot(date,hospitalises,color="blue")
plt.plot(date,nouvellesHospitalisations,color="red")
plt.plot(date,reanimation,color="green")
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + "./stats/stat2_output.json")
plt.show()