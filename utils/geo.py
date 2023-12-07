from geopy.geocoders import Nominatim


def get_city(lat, lon):
    geolocation = Nominatim(user_agent='test')
    return geolocation.reverse(f'{lat}, {lon}').address.split(',')[4]