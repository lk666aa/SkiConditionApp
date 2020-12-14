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
        Program will output will tell the user whether it suggests user to ski
        at the location.

        """

        address = input("Enter a ski resort name: ")
        lat, long = get_coordinates(address)
        stats = get_historical_weather(lat, long)
        snowfall = stats.get(SNOWFALL)
        temperature = stats.get(AVERAGE_TEMPERATURE)
        rainfall = stats.get(RAINFALL)

        if rainfall > RAINFALL_THRESHOLD:
            print("It is NOT a good time to go ski at " + address +
                  " because it has rained " + "{:.2f}".format(rainfall) +
                  "mm in the past 5 days. The amount of snowfall is "
                  + "{:.2f}".format(
                snowfall) + "mm and the average tempertures is "
                  + "{:.2f}".format(temperature) + " Celcius.")
        elif snowfall < SNOW_THRESHOLD and temperature > TEMPERATURE_THRESHOLD:
            print("It is NOT a good time to go ski at " + address +
                  " because there is " + "{:.2f}".format(snowfall) +
                  "mm snowfall and average temperatures are "
                  + "{:.2f}".format(temperature) +
                  " Celcius which means the snow has had a chance to melt. "
                  + "It has rained "
                  + "{:.2f}".format(rainfall) + "mm in the past 5 days.")
        elif snowfall >= SNOW_THRESHOLD and temperature <= TEMPERATURE_THRESHOLD:
            print("It is a GREAT time to go ski at " + address +
                  " because there is " + "{:.2f}".format(
                snowfall) + "mm snowfall and average temperatures are "
                  + "{:.2f}".format(
                temperature) + " Celcius which means the snow "
                  + "could not have melted. It has rained "
                  + "{:.2f}".format(rainfall) + "mm in the past 5 days.")
        else:
            print("PICK YOUR POISON at " + address +
                  " because there is " + "{:.2f}".format(
                snowfall) + "mm snowfall and average temperatures are "
                  + "{:.2f}".format(
                temperature) + " Celcius which means conditions can go "
                  + "either way. And the rainfall is "
                  + "{:.2f}".format(rainfall) + "mm.")
        print("\n")


app = SkiConditionsApp()
while True:
    app.getConditions()
