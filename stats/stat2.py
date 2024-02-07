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
index = 0
StepAxisX = []
for plot in data:
    if index % 15 == 0:
      StepAxisX.append(plot["date"])
    reanimation.append(plot["reanimation"])
    date.append(plot["date"])
    hospitalises.append(plot["hospitalises"])
    nouvellesHospitalisations.append(plot["nouvellesHospitalisations"])
    index+=1

plt.style.use('_mpl-gallery')
plt.plot(date,hospitalises,color="blue", label="hospitalises")
plt.plot(date,nouvellesHospitalisations,color="red", label="nouvelles hospitalisations")
plt.plot(date,reanimation,color="green", label="reanimation")
plt.xticks(StepAxisX, rotation=45)
plt.subplots_adjust(left=0.032, bottom=0.1)
plt.legend(loc='upper right', fontsize='x-large')
print("Statistique de nombre d'hospitalisations, de réanimations et de nouvelles hospitalisations par jour, en Île-de-France.")
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)
plt.show()