import requests
from datetime import datetime

ID = "graph01"
USERNAME = "exp"
TOKEN = "8K$k(9YE8C$cI)6uS"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph01",
    "name" : "Coding graph",
    "unit" : "code",
    "type" : "int",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" :TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config , headers=headers)
# print(response.text)



pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many code problems did you solve today? "),
}

response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"

new_pixel_data = {
    "quantity":"4"
}

# response = requests.put(url=update_pixel_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)
