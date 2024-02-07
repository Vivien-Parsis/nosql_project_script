import matplotlib.pyplot as plt
from datetime import datetime
import time
from query_stat_handler import mongodb_query_handler
start = time.time()
# Statistiques de nombre de décès, hospitalisation et cas confirmé par jour dans le monde.
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
filePath = "./stats/stat1_output.json"
query_handler = mongodb_query_handler(query,filePath)
data = query_handler.getOutputAggregate()
date, confirmes, gueris, deces = [],[],[],[]
index = 0
StepAxisX = []
for plot in data:
    if index % 15 == 0:
      StepAxisX.append(plot["date"])
    date.append(plot["date"])
    confirmes.append(plot["confirmes"])
    gueris.append(plot["gueris"])
    deces.append(plot["deces"])
    index+=1

plt.style.use('_mpl-gallery')
plt.plot(date,confirmes,color="green", label="confirmes")
plt.plot(date,deces,color="red", label="deces")
plt.plot(date,gueris,color="blue", label="gueris")
plt.legend(loc="upper right", fontsize="x-large")
plt.xticks(StepAxisX, rotation=45)
print("Statistiques de nombre de décès, hospitalisation et cas confirmé par jour dans le monde.")
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)
plt.show()