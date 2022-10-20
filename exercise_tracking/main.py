import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

app_id = "fd1eccab"
api_key = "03733c55b5a491a1f8e76c6e4427d73a"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint ="https://api.sheety.co/2edd9968c480a044aeadb3e2ece243ce/copyOfMyWorkouts/workouts"

today = dt.datetime.now()
time = today.strftime("%H:%M:%S")
date = today.strftime("%d/%m/%Y")



headers = {
 "x-app-id" : app_id,
 "x-app-key" : api_key,
 "Content-Type": "application/json",
 "x-remote-user-id": "0",
 "Authorization" : "Bearer qkdtjsdud12"
}

exercise_config = {
     "query" : input("Tell me what exercise you did: "),
     "gender":"female",
     "weight_kg":55,
     "height_cm":162,
     "age":30,
}



response = requests.post(url=endpoint,json=exercise_config,headers=headers)


data = response.json()["exercises"]
print(data)
for workout in data:
    exercise_workout = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" :workout["name"].title(),
            "duration" :workout["duration_min"],
            "calories" :workout["nf_calories"],
        }
    }

    response01 = requests.post(url=sheety_endpoint,json=exercise_workout,headers=headers)
    print(response01.text)