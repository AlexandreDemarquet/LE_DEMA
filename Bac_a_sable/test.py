import folium
import pandas as pd

df = pd.read_csv("/home/n7student/LE_DEMA/LE_DEMA/Bac_a_sable/pylones-rte.csv",delimiter=";")


map_osm = folium.Map(location=[48.85, 2.34])

df["Longitude pylône (DD)"]
for ind, lat, lon in df[['Latitude pylône (DD)', 'Longitude pylône (DD)']][:50].itertuples():
    map_osm.add_child(folium.RegularPolygonMarker(location=[lat,lon],
                       fill_color='#132b5e', radius=5))

map_osm.save("Map_pylone.html")