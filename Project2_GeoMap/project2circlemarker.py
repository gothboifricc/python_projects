import folium
import pandas

coords = pandas.read_csv("Volcanoes.txt")
lat = list(coords["LAT"])
lon = list(coords["LON"])
elev = list(coords["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

map_p = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    map_p.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el) + " m", fill_color=color_producer(el), color="grey", fill=True, fill_opacity=0.5))
map.add_child(map_p)

map.save("map1.html")
