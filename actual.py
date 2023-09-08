import requests
import json
import numpy as np


api_key = 'cd4259afc066461f96e40d56cdc6fe76'

#For Porvoo
lat = 60.3954
lon = 25.6605

#city weather now
api_urlw = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
response = requests.get(api_urlw)
dataw = response.json()
temp = dataw['main']['temp']-273
wspeed = dataw['wind']['speed']
hum = dataw['main']['humidity']

#write the new line of actual weather
newrowACT=np.array([temp, wspeed, hum])
fromACT = np.loadtxt("ACTUAL.txt")
sumACT=np.vstack((fromACT, newrowACT))


'''city coordinates
city = input("enter city ")
api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
response = requests.get(api_url)
data = response.json()
jy = data[0]
lat = jy["lat"]
lon = jy["lon"]
print(lat)
print(lon)'''