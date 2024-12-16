import requests

response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')


if response.status_code == 200:
    json_data = response.json()  
    print("Danh sách các bình luận nổi bật:")
    
    for i in range(min(3, len(json_data))):
        bl = json_data[i]
        print(f"\nBình luận {i + 1}:")
        print("ID:", bl['id'])
        print("Tên:", bl['name'])
        print("Email:", bl['email'])
        print("Nội dung:", bl['body'])
        print("==================================")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
