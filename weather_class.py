
class WeatherClass: 
    def __init__(self, time, summary, windSpeed, temperature, uvIndex, visibility):
        self.time = time 
        self.summary = summary 
        self.windSpeed = windSpeed 
        self.temperature = temperature
        self.uvIndex = uvIndex 
        self.visibility = visibility 
        
    def __str__(self):
        return 'weather'