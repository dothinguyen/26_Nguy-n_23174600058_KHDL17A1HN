import json

data = {
    "1_ten": "Nguyễn Văn A",
    "1_nam_sinh": 2003,
    "2_ten": "Trần Văn C",
    "2_nam_sinh": 2003,
    "3_ten": "Lê Thị B",
    "3_nam_sinh": 2004
}

json_string = json.dumps(data, ensure_ascii=False, indent=4)

print(json_string)
print(type(json_string))