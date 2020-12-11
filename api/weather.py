
import requests
import datetime

from constants import WEATHER_API_KEY, SNOWFALL, AVERAGE_TEMPERATURE, RAINFALL

UNITS = 'metric'


def get_historical_weather(lat, long):
    """
    Main function for calculating the weather statistics.
    Takes latitude and longitude, and return the data of rainfall,
    temperature and snowfall of the location.

       Parameters
       ----------
       param1
            lat : float
       param2
            long : float

       Returns
       -------
       Dictionary
           stats : data of rainfall, temperature and snowfall of the location

    """
    dates = get_past_5_dates()

    historical_weather = []
    for date in dates:
        date = str(date.timestamp())[:10]
        data = get_weather_data(lat, long, date)

        # hourly instead of current because hourly gives us a more complete snapshot of historical weather data
        historical_weather.append(data.json()['hourly'])
    return aggregate_weather_stats(historical_weather)


def get_weather_data(lat, long, date):
    """
    https://openweathermap.org/api/one-call-api
    Use API to get weather statistics and return it.
      Parameters
      ----------
      param1
            lat : float
      param2
            long : float
      param3
            date : integer (unix time)
      Returns
      -------
      Dictionary
          A nested dictionary that contains all weather information

    """

    return requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat='
                     + str(lat) + '&lon=' + str(long) + '&dt=' + date + '&appid='
                     + WEATHER_API_KEY + '&units=' + UNITS)

def get_past_5_dates():
    """
    Return a list of datetime object of past 5 days.

      Parameters
      ----------

      Returns
      -------
      List
          dates: list of datetime object of past 5 days

    """

    today = datetime.datetime.now()
    dates = []
    for x in range(1,6):
        dates.append(today - datetime.timedelta(days=x))
    return dates


def aggregate_weather_stats(historical_weather):
    """
    Function that parse the data in historical_weather. Returns the data of rainfall,
    temperature and snowfall of the location.

      Parameters
      ----------
      param1
            historical_weather: Dictionary
      Returns
      -------
      Dictionary
            stats: A dictionary that contains all weather information

    """
    stats = {}

    total_snowfall = 0
    total_temp = 0
    total_temp_count = 0
    total_rainfall = 0
    for day in historical_weather:
        for hour in day:
            if hour.get('snow') and hour.get('snow').get('1h'):
                total_snowfall += hour['snow']['1h']
            if hour.get('temp'):
                total_temp += hour.get('temp')
                total_temp_count += 1
            if hour.get('rain') and hour.get('rain').get('1h'):
                total_rainfall += hour['rain']['1h']
    average_temp = total_temp / total_temp_count
    stats[SNOWFALL] = total_snowfall
    stats[AVERAGE_TEMPERATURE] = average_temp
    stats[RAINFALL] = total_rainfall
    return stats
