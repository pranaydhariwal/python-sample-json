import json
from decimal import Decimal
 
json_input = '{"persons": [{"name": "1.234", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'

try:
  decoded = json.loads(json_input)

  for x in decoded["persons"]:
    print(x['name'])

except TypeError as e:
  print(e)