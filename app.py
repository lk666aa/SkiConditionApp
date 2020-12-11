
from api.google_maps import get_coordinates
from api.weather import get_historical_weather
from constants import SNOWFALL, AVERAGE_TEMPERATURE, RAINFALL, \
    SNOW_THRESHOLD, TEMPERATURE_THRESHOLD, RAINFALL_THRESHOLD


class SkiConditionsApp:

    def __init__(self):
        pass

    def getConditions(self):
        """Main function to run the ski condition app

        Program will ask the user to input an address in String.
        Program will output will tell the user whether it suggests user to ski at the location.

        """

        address = input("Enter a ski resort name: ")
        lat, long = get_coordinates(address)
        stats = get_historical_weather(lat, long)
        print(lat,long)
        snowfall = stats.get(SNOWFALL)
        temperature = stats.get(AVERAGE_TEMPERATURE)
        rainfall = stats.get(RAINFALL)

        if rainfall > RAINFALL_THRESHOLD:
            print("It is NOT a good time to go ski at " + address +
                  " because it has rained " + str(rainfall) + "mm in the past 5 days")
        elif snowfall < SNOW_THRESHOLD and temperature > TEMPERATURE_THRESHOLD:
            print("It is NOT a good time to go ski at " + address +
                  " because there is " + str(snowfall) + "mm snowfall and average temperatures are "
                  + str(temperature) + " Celcius which means the snow has had a chance to melt.")
        elif snowfall >= SNOW_THRESHOLD and temperature <= TEMPERATURE_THRESHOLD:
            print("It is a GREAT time to go ski at " + address +
                  " because there is " + str(snowfall) + "mm snowfall and average temperatures are "
                  + str(temperature) + " Celcius which means the snow could not have melted.")
        else:
            print("PICK YOUR POSITION at " + address +
                  " because there is " + str(snowfall) + "mm snowfall and average temperatures are "
                  + str(temperature) + " Celcius which means conditions can go either way.")
        print("\n")


app = SkiConditionsApp()
while True:
    app.getConditions()
