from query_handler import mongodb_query_handler
import time
start = time.time()

# Obtenir le nombre de personnes hospitalisées en réanimation le jour du bulletin. Remplacer date pour avoir le jour qu’on veut
aggregate = []
filePath = "./requests/req2_output.json"

find= {"date":"2020-01-01"}
findProject = {"date":1,"hospitalises":1,"_id":0}
description = "Obtenir le nombre de personnes hospitalisees en reanimation le jour du bulletin. Remplacer date pour avoir le jour qu'on veut"
req = mongodb_query_handler(aggregate,filePath,find,findProject)
req.getOutputFind()
print(description)
print("successfully executed script, execution time : " + str(round(time.time() - start,2))+ "ms")
print("output result can be found in " + filePath)