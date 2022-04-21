import json
from sqlalchemy import false

from yaml import parse

# load() :  loads a json file
# loades() : for parsing the json string to in json data

data = '{"var1":"harry","var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

# json.dump() : 

data2 = {
    "channel_name":"code_with_harry",
    "cars" : ["BMW","Audy","Maruti"],
    "Fidge":("roti",540),\
    "isbad":False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task = what is sort keys parameter in dumps