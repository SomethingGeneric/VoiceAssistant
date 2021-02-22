from assistant_utils import speak, sanitize

import urllib, requests, json


class weather:
    def __init__(self):
        self.triggers = ["weather"]

    def run(self, raw):
        search = sanitize(self.triggers, raw)

        speak("Getting weather data for: " + search)

        try:

            save = search

            search = urllib.parse.quote(search)

            commandstr = "http://api.weatherstack.com/current?access_key=KEY&query=QUERY&units=f".replace(
                "KEY", "f35006ff9cb12a5d660572cb4791508f"
            ).replace(
                "QUERY", search
            )

            data = json.loads(requests.get(commandstr).text)

            things = data["current"]

            data = [
                "The temperature is " + str(things["temperature"]) + " degrees",
                "It feels like " + str(things["feelslike"]) + " degrees",
                "The conditions are " + things["weather_descriptions"][0],
                "The wind speed is " + str(things["wind_speed"]) + " miles per hour",
                "There is " + str(things["precip"]) + " percent precipitation",
                "It is " + str(things["humidity"]) + " percent humid",
                "The cloud cover percent is " + str(things["cloudcover"]) + " percent",
                "There are " + str(things["visibility"]) + " miles of visibility",
            ]

            final_message = "Here's the weather for " + save + "\n"

            for item in data:
                final_message += item + "\n"

            speak(final_message)

        except Exception as e:
            speak("Had an error getting weather data: " + str(e))
