import requests
from twilio.rest import Client
sid = "AC51e7fee3e3808c9ea259518c4cb50cf9"
token = "0cce25480838a732a52e584c5db263f5"
cl = Client(sid, token)

PARAMS = {
    "lat": 55.660095,
    "lon": 37.219522,
    "exclude": "current,minutely,daily",
    "appid": "8c0cba31b052ae6c7318e7a9f8a2a724",
}
weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=PARAMS)
weather.raise_for_status()
weathers = weather.json()
slices = weathers["hourly"][:12]
def message():
    for i in slices:
        if i["weather"][0]["id"] < 700:
            return "Bring an umbrella☂️☂️☂️"


msg = cl.messages.create(
    body=message(),
    from_="+12019043526",
    to="+79017069674"
)

print(msg.status)