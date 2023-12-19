import streamlit as st
import pandas as pd
import numpy as np
from st_combobox import st_combobox
from streamlit_folium import st_folium, folium_static
from dotenv import load_dotenv
import requests
import folium
import os

load_dotenv()

st.title('MapQuest Explorer PH')

def get_city_choices(query: str):
    url = "https://www.mapquestapi.com/search/v2/radius"
    params = {
        "key": os.getenv('API_KEY'),
        "origin": query,
        "radius": "50",  # Adjust the radius as needed
        "maxMatches": "5",  # Limit the number of results
        "country": "PH",  # Limit the search to the Philippines
        "category": "ADM1",  # Filter by cities
    }
    response = requests.get(url, params=params)
    data = response.json()

    options = []
    try:
        if data is not None:
            for location in data["collections"][0]:
                city = location["adminArea5"]
                province = location["adminArea4"]
                options.append(f"{city}, {province}")
    except:
        st.warning("No Locations Found.")
    
    st.write(options)

    return options

def get_directions(start_location, end_location):
    url = "https://www.mapquestapi.com/directions/v2/route"
    params = {
        "key": os.getenv('API_KEY'),
        "from": start_location,
        "to": end_location,
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "route" in data:
        return data["route"]["legs"][0]["maneuvers"]  # Extract maneuvers from the response
    else:
        return None
    
def plot_directions_on_map(maneuvers):
    if not maneuvers:
        st.warning("Directions not available.")
    
    # Create a Folium map centered around the first maneuver's start location!
    map_center = [maneuvers[0]["startPoint"]["lat"], maneuvers[0]["startPoint"]["lng"]]
    folium_map = folium.Map(location=map_center, zoom_start=13)

    # Plot each maneuver as a marker on the map
    for maneuver in maneuvers:
        location = [maneuver["startPoint"]["lat"], maneuver["startPoint"]["lng"]]
        folium.Marker(location, popup=maneuver["narrative"]).add_to(folium_map)

    # Display the Folium map using Streamlit
    folium_static(folium_map)

main = st.container()

with main:
    from_location = st_combobox(key="from_combobox", 
                                search_function=get_city_choices, 
                                label="From Location", 
                                placeholder="Your Current Location", 
                                rerun_on_update=True)

    to_location = st_combobox(key="to_combobox",
                              search_function=get_city_choices, 
                              label="To Location", 
                              placeholder="Your Goal Destination", 
                              rerun_on_update=True)

    if st.button('Get Instructions', use_container_width=True):
        maneuvers = get_directions(from_location, to_location)
        plot_directions_on_map(maneuvers)

        


