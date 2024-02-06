from req_class import mongo_req

# Obtenir le nombre de personnes hospitalisées en réanimation le jour du bulletin. Remplacer date pour avoir le jour qu’on veut
aggregate = []
filePath = "./requests/req2_output.json"

find= {"date":"2020-01-01"}
findProject = {"date":1,"hospitalises":1,"_id":0}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputFind()