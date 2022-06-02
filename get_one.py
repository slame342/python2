import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
Get_one = response.content.decode()
print(Get_one)

with open('get_one.json', 'w') as file:
    json.dump(Get_one, file)
    print(type(Get_one))

response = requests.get("https://jsonplaceholder.typicode.com/posts")
content = response.content
print(response.status_code)
get_one = content.decode()
userId = json.loads(get_one)
print(type(file))

for user in userId:
    with open(f'pars/get_one_{user["userId"]}.json', 'w') as file:
        json.dump(user, file)
print(get_one)



