#24 JSON complex object
import json

json_string = input("Enter JSON string: ")
try:
    data = json.loads(json_string)
    if isinstance(data, (dict, list)):
        print("JSON contains a complex object")
    else:
        print("JSON does not contain a complex object")
except json.JSONDecodeError:
    print("Invalid JSON")
