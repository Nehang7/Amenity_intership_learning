import json
data ={
    "Name":"prince",
    "age":22,
    "city":"rajkot",
    
}

with open('examplejson.json','w')as f:
    json.dump(data,f,indent=4)#dump convert any python objects into json

    print("done")

with open('examplejson.json','r')as r:
   read=json.load(r)#load parse json string
   print(read)
