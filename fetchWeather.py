
from weather import *
from requests import *

key="65b916b412446984e05f74fae15c1b4f"

def fetch(city):

    url="https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API}"
    url=url.format(city=city,API=key)

    result=get(url)
    result=result.json()

    city=result["name"]
    temp = result["main"]["temp"]
    weater=result["weather"][0]["main"]

    wea=weather(city,temp,weater)
    return wea
