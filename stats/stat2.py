import matplotlib.pyplot as plt
from datetime import datetime
import time
from query_stat_handler import mongodb_query_handler
start = time.time()
# Statistique de nombre d’hospitalisations, de réanimations et de nouvelles hospitalisations par jour, en Île-de-France.
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
filePath = "./stats/stat2_output.json"
query_handler = mongodb_query_handler(query,filePath)
data = query_handler.getOutputAggregate()
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
print("Statistique de nombre d'hospitalisations, de réanimations et de nouvelles hospitalisations par jour, en Île-de-France.")
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)
plt.show()