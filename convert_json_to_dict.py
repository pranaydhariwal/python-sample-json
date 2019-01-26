import json
json_data = '{"name1":"sanjay", "name2":"harsh", "name3":"ansupadh"}'
python_obj = json.loads(json_data)
print(python_obj["name1"])
print(python_obj["name2"])

#print "bethere"