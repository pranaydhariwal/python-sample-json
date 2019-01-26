import json
from decimal import Decimal

json_data = '{"price":"1.245"}'
python_obj = json.loads(json_data, parse_float=Decimal)

print(python_obj['price'])
