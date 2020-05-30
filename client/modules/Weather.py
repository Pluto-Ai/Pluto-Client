# -*- coding: utf-8-*-
import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
import json
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["WEATHER", "TODAY", "TOMORROW"]

def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(weathers?|temperature|forecast|outside|hot|' +
                          r'cold|jacket|coat|rain)\b', text, re.IGNORECASE))

def get_forecast_by_lat_long(latitude, longitude):
    """
    Using OpenWeatherMap API via rapidapi, grab weather forecast data
    """
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {
            "lat":latitude,
            "lon":longitude,
            "units":"imperial"
            }

    headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "cab2202dc7mshd662efa8fb2687bp118d60jsn00979f6e2cc9"
            }

    response = requests.request("GET", url, headers=headers, params=querystring)
    weather = response.json()['weather'][0]

    return "Currently, the weather is {} with {}".format(weather['main'], weather['description'])

def handle(text, mic, profile):
    """
    Responds to user-input, typically speech text, with a summary of
    the relevant weather for the requested date (typically, weather
    information will not be available for days beyond tomorrow).

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    forecast = None
    if 'latitude' in profile and 'longitude' in profile:
        forecast = get_forecast_by_lat_long(str(profile['latitude']), str(profile['longitude']))

    if not forecast:
        mic.say("I'm sorry, I can't seem to access that information. Please " +
                "make sure that you've set your location on the dashboard.")
        return

    mic.say(forecast)
    return

