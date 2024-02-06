from req_class import mongo_req

# Obtenir le nombre de cas confirmé selon une région ou département et date choisis
aggregate = []
filePath = "./requests/req3_output.json"

find, findProject = {"casConfirmes":{"$exists":"true"},"nom":"Île-de-France","date":"2020-03-24"},{"nom":1,"casConfirmes":1,"_id":0}
req = mongo_req(aggregate,filePath,find,findProject)
req.getOutputFind()