import datetime
import unittest
from unittest.mock import patch
from api.weather import get_past_5_dates, aggregate_weather_stats, \
    get_historical_weather


class MockWeatherData:
    """
    Mock weather data object that allows us to unit test `get_historical_weather`
    """

    def json(self):
        return {
            'hourly': [
                {
                    'snow': {
                        '1h': 3
                    },
                    'temp': 2,
                    'rain': {
                        '1h': 1
                    }
                }
            ]
        }


class Test(unittest.TestCase):
    @patch('api.weather.get_weather_data')
    def test_get_historical_weather(self, get_weather_data):
        """
        Mock the openweather api call for better unit testing of the function.
        """
        get_weather_data.return_value = MockWeatherData()
        response = get_historical_weather(1, 1)
        expected_response = {'snowfall': 15, 'average_temperature': 2.0,
                             'rainfall': 5}

        assert response == expected_response

    def test_get_past_5_dates(self):
        """
        Test if the get_past_5_dates() works properly.
        """
        dates = get_past_5_dates()
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=1)
        five_days_ago = today - datetime.timedelta(days=5)
        assert len(dates) == 5
        assert yesterday.day == dates[0].day
        assert five_days_ago.day == dates[4].day

    def test_aggregate_weather_stats(self):
        """
        Mock a historical_weather data and test aggregate_weather_stats() function.
        """
        historical_weather = [
            [{
                "dt": 1586390400,
                "temp": 2.3,
                "feels_like": 269.43,
                "pressure": 1006,
                "humidity": 65,
                "dew_point": 272.46,
                "clouds": 0,
                "wind_speed": 9.83,
                "wind_deg": 60,
                "wind_gust": 15.65,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ]
            }]
        ]

        stats = aggregate_weather_stats(historical_weather)
        expected_stats = {'snowfall': 0, 'average_temperature': 2.3,
                          'rainfall': 0}
        assert stats == expected_stats
