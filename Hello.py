# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import requests


LOGGER = get_logger(__name__)


def run():

# Define the app's layout
st.title("Places to Visit")
st.write("This app recommends places to visit in a city of your choice.")

# Get the user's input
city = st.text_input("Enter the city you would like to visit:")

# Make a request to the OpenWeatherMap API to get the city's latitude and longitude
url = "https://api.openweathermap.org/geo/1/direct?q=" + city + "&appid=YOUR_API_KEY"
response = requests.get(url)
data = response.json()

# Get the city's latitude and longitude
latitude = data["lat"]
longitude = data["lon"]

# Make a request to the Foursquare API to get a list of places of interest in the city
url = "https://api.foursquare.com/v2/venues/explore?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&v=20200914&ll=" + str(latitude) + "," + str(longitude) + "&radius=5000&category=tourist_attraction"
response = requests.get(url)
data = response.json()

# Get the list of places of interest
places = data["response"]["groups"][0]["items"]

# Display the list of places of interest to the user
st.write("Here are some places of interest in " + city + ":")
for place in places:
    name = place["name"]
    category = place["categories"][0]["name"]
    st.write(name + " (" + category + ")")

if __name__ == "__main__":
    run()
