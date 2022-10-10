import json
with open("sample.json") as JsonFile:
    data=json.load(JsonFile)
    jsondata=data("server")
    for x in jsondata:
        header=x.keys()
        print(header)
        values=x.values()
        print(values)