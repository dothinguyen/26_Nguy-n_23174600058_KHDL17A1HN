import json

json_string_1 = '{"name":"Nguyễn Văn A","age":18}'
json_string_2 = '{"name":"Lê Văn C","age":13}'

json_object_1 = json.loads(json_string_1)
json_object_2 = json.loads(json_string_2)

print(json_object_1)
print(json_object_2)
