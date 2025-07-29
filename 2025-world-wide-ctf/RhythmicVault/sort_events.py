import json
from pprint import pprint

data = ""
with open("task.rdlevel","rb") as f:
    data = json.load(f)

events = data["events"] 
events = sorted(events,key=lambda x: x.get("beat",-1))


print(events)