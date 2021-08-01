
class weather:

    def __init__(self,city,temp,weather):
        self.city_name  =city
        self.temperature=temp
        self.weather    =weather

    def get_city_name(self):
        return self.city_name

    def get_temperature(self):
        return self.temperature

    def get_weather(self):
        return self.weather
