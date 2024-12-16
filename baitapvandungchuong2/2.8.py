import json

data = {
    "ten1": "Nguyễn Văn A",
    "nam_sinh1": 2005,
    "ten2": "Trần Thị B",
    "nam_sinh2": 2006,
    "ten3": "Lê Bá C",
    "nam_sinh3": 2007
}

json_string= json.dumps(data, ensure_ascii=False)

print(json_string)
print(type(json_string))