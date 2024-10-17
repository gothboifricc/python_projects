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

map_v = folium.FeatureGroup(name="Weird Volcanoes")
map_p = folium.FeatureGroup(name="Populations dude")

for lt, ln, el in zip(lat, lon, elev):
    map_v.add_child(folium.Marker(location=[lt, ln],popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

map_p.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(map_v)
map.add_child(map_p)

map.add_child(folium.LayerControl())
map.save("map1.html")
