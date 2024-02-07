from query_handler import mongodb_query_handler
import sys

requests = {
    "req1":{
        "handler":mongodb_query_handler(filePath="./requests/output/req1_output.json",aggregate=[{"$match":{"nom":"France"}},{"$group":{"_id":"France","totalCasConfirme":{"$sum":"$casConfirmes"},"totalDeces":{"$sum":"$deces"},"totalGueris":{"$sum":"$gueris"},}},{"$project":{"pays":"$_id","_id":0,"totalCasConfirme":1,"totalDeces":1,"totalGueris":1}}]),
        "FindOrAggregate":"aggregate",
        "description":"Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France"
    },
    "req2":{
        "handler":mongodb_query_handler(filePath="./requests/output/req2_output.json",findMatch={"date":"2020-01-01"},findProject={"date":1,"hospitalises":1,"_id":0}),
        "FindOrAggregate":"find",
        "description":"Obtenir le nombre de personnes hospitalisées en réanimation le jour du bulletin. Remplacer date pour avoir le jour qu'on veut"
    },
    "req3":{
        "handler":mongodb_query_handler(filePath="./requests/output/req3_output.json",findMatch={"casConfirmes":{"$exists":"true"},"nom":"Île-de-France","date":"2020-03-24"},findProject={"nom":1,"casConfirmes":1,"_id":0}),
        "FindOrAggregate":"find",
        "description":"Obtenir le nombre de cas confirmé selon une région ou département et date choisis"
    },
    "req4":{
        "handler":mongodb_query_handler(filePath="./requests/output/req4_output.json",aggregate=[{"$match":{"code":{"$regex":"DEP-.*"}}},{"$group":{"_id":"$nom","totalHospitalises":{"$sum":"$hospitalises"},}},{"$sort":{"totalHospitalises":-1}},{"$project":{"departement":"$_id","_id":0,"totalHospitalises":1}}]),
        "FindOrAggregate":"aggregate",
        "description":"Affiche le nombre hospitalisation total par département"
    },
    "req5":{
        "handler":mongodb_query_handler(filePath="./requests/output/req5_output.json",aggregate=[{"$match":{"code":{"$regex":"REG-.*"}}},{"$group":{"_id":"$nom","deces":{"$sum":"$deces"},"gueris":{"$sum":"$gueris"}}},{"$project":{"_id":0,"region":"$_id","deces":1,"gueris":1}},{"$sort":{"region":1}}]),
        "FindOrAggregate":"aggregate",
        "description":"Affiche le nombre de décès et de guéris totaux par régions"
    },
    "req6":{
        "handler":mongodb_query_handler(filePath="./requests/output/req6_output.json",aggregate=[{"$facet":{"minVal":[{"$match":{"code":{"$regex":"DEP-.*"}}},{"$group":{"_id":"$nom","deces":{"$sum":"$deces"}}},{"$sort":{"deces":1}},{"$limit":1},{"$project":{"departement":"$_id","_id":0,"deces":1}},],"maxVal":[{"$match":{"code":{"$regex":"DEP-.*"}}},{"$group":{"_id":"$nom","deces":{"$sum":"$deces"}}},{"$sort":{"deces":-1}},{"$limit":1},{"$project":{"departement":"$_id","_id":0,"deces":1}}]}},{"$project":{"min":{"$first":"$minVal"},"max":{"$first":"$maxVal"}}}]),
        "FindOrAggregate":"aggregate",
        "description":"Affiche le département avec le moins et le plus de décès de covid"
    },
    "req7":{
        "handler":mongodb_query_handler(filePath="./requests/output/req7_output.json",aggregate=[{"$match":{"nom":"France"}},{"$group":{"_id":"France","totalReanimation":{"$sum":"$reanimation"},"totalHospitalisation":{"$sum":"$hospitalises"},"totalGueris":{"$sum":"$gueris"}}},{"$project":{"_id":0,"pays":"$_id","PartDeRea":{"$round":[{"$divide":["$totalHospitalisation","$totalReanimation"]},2]},"totalDeReanimation":"$totalReanimation","totalDeHospitalisation":"$totalHospitalisation"}}]),
        "FindOrAggregate":"aggregate",
        "description":"Affiche sur l'ensemble du covid en France, le pourcentage de réanimations dans les hospitalisés."
    },
    "req8":{
        "handler":mongodb_query_handler(filePath="./requests/output/req8_output.json",aggregate=[{"$facet":{"nombreDeJours":[{"$group":{"_id":"$date"}},{"$count":"nombredejours"},],"debut":[{"$group":{"_id":"$date"}},{"$sort":{"_id":1}},{"$limit":1}],"fin":[{"$group":{"_id":"$date"}},{"$sort":{"_id":-1}},{"$limit":1}]}},{"$project":{"nombredejours":{"$getField":{"field":"nombredejours","input":{"$first":"$nombreDeJours"}}},"debut":{"$getField":{"field":"_id","input":{"$first":"$debut"}}},"fin":{"$getField":{"field":"_id","input":{"$first":"$fin"}}}}}]),
        "FindOrAggregate":"aggregate",
        "description":"Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France"
    }
}
def getRequests():
    if len(sys.argv)==2:
        secondArg = sys.argv[1]
        if "r=" not in secondArg:
            print("invalid argument")
            return
        CurrentReq = secondArg.split("=")[1]
        if CurrentReq not in requests.keys():
            print("request not found")
            return
        CurrentReq = requests[CurrentReq]
        if CurrentReq["FindOrAggregate"] != "aggregate" and CurrentReq["FindOrAggregate"] != "find":
            print("request invalid")
            return
        elif CurrentReq["FindOrAggregate"] == "aggregate":
            print(CurrentReq["description"])
            print("les résultats de la requete mongoDB peuvent être trouvé dans le fichier : " + CurrentReq["handler"].getFilePath())
            CurrentReq["handler"].getOutputAggregate()
        else:
            print(CurrentReq["description"])
            print("les résultats de la requete mongoDB peuvent être trouvé dans le fichier : " + CurrentReq["handler"].getFilePath())
            CurrentReq["handler"].getOutputFind()
    else:
        print("missing r=<request> argument")
    
getRequests()