import json
with open("sample.json") as x:
    data=json.load(x)
    jsondata=data("server")
    for i in jsondata:
        values=i.values()
        print(values)
