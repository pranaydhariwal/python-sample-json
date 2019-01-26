import json
array = '{"names":["ram","shyam","krishna"]}'

python_obj = json.loads(array)

for element in python_obj["names"]:
  print(element)