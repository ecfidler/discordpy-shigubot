'''
weather forecast script, made with PyOWM

Registries
Columbus :: <pyowm.weatherapi25.location.Location - id=4509177, name=Columbus, lon=-82.998787, lat=39.961182>
Cincinnati :: <pyowm.weatherapi25.location.Location - id=4508722, name=Cincinnati, lon=-84.456886, lat=39.161999>
Dayton :: id=4509884

'''

from pyowm import OWM
import discord

def getText(file):
    with open(file, "r") as f:
        lines = f.read()
        return lines.strip()

owm = OWM(getText(".\\keychain\\owmkey.txt"))

LocationIds = {
        "columbus":4509177,
        "cincinnati":4508722,
        "dayton":4509884,
        "pittsburgh":5206379
}

#obs = owm.weather_at_place("Columbus,US") # creates observation object
def getWeather(Location):

        id = LocationIds[Location]

        obs = owm.weather_at_id(id)

        w = obs.get_weather() # creates weather object
        status = w.get_detailed_status()
        temp_dict = w.get_temperature('fahrenheit')
        current_temp = temp_dict["temp"]
        icon_url = w.get_weather_icon_url()
        dt = w.get_reference_time(timeformat='iso')[:-6]
        title = "Weather in " + Location + " at " + dt
        url = "https://openweathermap.org/city/" + str(id)
        desc = "The Weather is currently: " + status
        daily_temp = "High: " + str(int(temp_dict["temp_max"])) + "| Low: " + str(int(temp_dict["temp_min"]))
        wind_dict = w.get_wind()
        wind_speed = wind_dict["speed"]

        weatherEmbed=discord.Embed(title=title, description=desc, color=0x1c57e3)
        weatherEmbed.set_author(name="Shigure's Forecast", url=url, icon_url="attachment://icon.png") # Change the icon back to shigure
        weatherEmbed.set_thumbnail(url=icon_url)
        weatherEmbed.add_field(name="Current Tempterture (F)", value=current_temp, inline=True)
        weatherEmbed.add_field(name="Daily Tempterture (F)", value=daily_temp, inline=True)
        weatherEmbed.add_field(name="Wind Speed (mph)", value=wind_speed, inline=True)
        weatherEmbed.set_footer(text="Message @fops#1969 if you have any questions")
        return weatherEmbed

'''
#testing
obs = owm.weather_at_id(4509177)
w = obs.get_weather()
print(w.get_temperature('fahrenheit'))
'''