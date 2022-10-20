import os
import requests
from twilio.rest import Client

Own_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "5e65f82e57d6f3a3c737d811e890bc48"
account_sid ="AC9b5946bcb005dd91c842be5f626be1df"
auth_token = "c386e2f085c1824acc69d05c08898c4b"

weather_param = {
    "lat" : 35.871433,
    "lon" : 128.601440,
    "appid" : API_KEY,
    "exclude" : "current,minutely,daily",
}

response = requests.get(Own_Endpoint,params=weather_param)
response.raise_for_status()

data = response.json()
weather = data["hourly"][:12]

will_rain = False

for hour in weather:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages \
       .create(
       body="It's going to rain today. Remember to bring an umbrella with you!",
       from_="+13605648536",
       to="+821023097903"
   )
   print(message.status)
#     weather_id_list.append(weather_id[0]['id'])
#
# for i in weather_id_list:
#     if i < 700:
#         print("Bring an umbrella")