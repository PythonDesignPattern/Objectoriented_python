import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}, "address": {"city": "Ahmedabad",' \
       '"pincode": 382345, "country": "india", "state": "gujrat"}, "stock": ["abc", "pqr", "def", "lml"]}'

# list_data = '["abc", "pqr", "def", "lml"]'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

# print x.name, x.hometown.name, x.hometown.id, x.address.city
for single_stock_list in x.stock:
    pass
    # print single_stock_list


# to reuse it # while developing application | webservice
def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

real_object = json2obj(data)
print real_object.name