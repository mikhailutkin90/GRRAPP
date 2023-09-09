import requests
import json
import numpy as np

#write the new line of actual weather

def get_my_data(api_urlw):
    '''docstring'''
    response = requests.get(api_urlw)
    dataw = response.json()
    temp = dataw['main']['temp']-273
    wspeed = dataw['wind']['speed']
    hum = dataw['main']['humidity']
    return temp, wspeed, hum

def crunch_data(temp, wspeed, hum):
    '''Return sumACT (wtf is sum_act)'''
    newrow_act = np.array([temp, wspeed, hum])
    from_act = np.loadtxt("ACTUAL.txt")
    sum_act = np.vstack((from_act, newrow_act))
    return sum_act


if __name__ == "__main__":
    api_key = 'cd4259afc066461f96e40d56cdc6fe76' # <-- change this to ENV var

    #For Porvoo
    lat = 60.3954
    lon = 25.6605

    #city weather now
    api_urlw = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    temp, wspeed, hum = get_my_data(api_urlw)
    sum_act = crunch_data(temp, wspeed, hum)
    print("Sum act is: ", sum_act)


'''city coordinates
city = input("enter city ")
api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
response = requests.get(api_url)
data = response.json()
jy = data[0]
lat = jy["lat"]
lon = jy["lon"]'''
