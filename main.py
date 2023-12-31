import streamlit as st
import pandas as pd
import csv
import plotly.express as px


file_path = 'LongLat79.csv'

st.set_page_config("Don's Whale Data 1979", page_icon=":whale:", layout='wide')

df_longlat = pd.read_csv(file_path)    
         
st.title("Don Ljungblad Whale Research and Sighting Data")
st.subheader('Northern Alaska: Fall of 1979')

fig = px.scatter_mapbox(df_longlat, lat='LAT', lon='LON', color='Season', zoom=5, hover_name='Year', hover_data=['Season', 'LAT', 'LON'], color_discrete_sequence=px.colors.qualitative.Light24)
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        },
        {
            "sourcetype": "raster",
            "sourceattribution": "Government of Canada",
            "source": ["https://geo.weather.gc.ca/geomet/?"
                       "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                       "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        }
      ])
fig.update_layout(height=1000)

st.plotly_chart(fig, use_container_width=True)
     
