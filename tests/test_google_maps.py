
import unittest
from unittest.mock import patch
from api.google_maps import get_coordinates


class Test(unittest.TestCase):

    @patch('googlemaps.Client.geocode')
    def test_get_historical_weather(self, geocode):
        """
        Mock the googlemaps api call for better unit testing of the function.
        """
        geocode.return_value = [
            {
                'geometry': {
                    'location': {
                        'lat': 1,
                        'lng': 1
                    }
                }
            }
        ]
        response = get_coordinates("Aspen")
        expected_response = 1, 1
        assert response == expected_response

