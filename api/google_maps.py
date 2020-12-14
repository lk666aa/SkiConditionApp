
import googlemaps

from constants import GOOGLE_MAPS_API_KEY


def get_coordinates(address):
    """
    https://pypi.org/project/googlemaps/1.0.2/
    Function that will return the longitude and latitude of the given input
    address

    Parameters
    ----------
    param1
        address:String

    Returns
    -------
    Float
        lat: latitude of the address
        long: longitude of the address

    """
    gmaps = googlemaps.Client(GOOGLE_MAPS_API_KEY)
    response = gmaps.geocode(address)

    lat = response[0]['geometry']['location']['lat']
    long = response[0]['geometry']['location']['lng']

    return lat, long
