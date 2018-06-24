import folium
import pandas
import mysql.connector
from mysql.connector import errorcode


def mysql_con():
    try:
        cnx = mysql.connector.MySQLConnection(user='developer', password='dev',
                                     host='10.10.10.2',
                                     port=3306,
                                     database='university')
        print("All works fine")
        data=pandas.read_sql("SELECT * FROM TABLE_NAME", con=cnx)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()

    name=list(data["University"])
    rate=list(data["Rate"])
    lat=list(data["Lat"])
    lon=list(data["Lon"])
    return lat, lon, name, rate


def color_mark(rate):
    if rate<0:
        raise ValueError("Rate cannot be < 0")
    if rate>8.0:
        return "green", "check"
    elif 5.0 <= rate <= 8.0:
        return "orange", "cloud"
    else:
        return "red", "info-sign"

#Start point on map
def main():
    nau_position=[50.439895, 30.430243]
    map=folium.Map(location=nau_position, zoom_start=5)
    fg_name=folium.FeatureGroup(name="University Name")
    lat, lon, name, rate=mysql_con()
    #Show Markers on map
    for lt, ln, nm, rt in zip(lat, lon, name, rate):
        color_temp, icon_temp=color_mark(rt)
        fg_name.add_child(folium.Marker(location=[lt, ln], popup=str(nm + "\n" + str(rt)), icon=folium.Icon(color=color_temp, icon=icon_temp)))

    fg_poligon=folium.FeatureGroup(name="Poligon")
    fg_poligon.add_child(folium.GeoJson(data=open('data/countries.geo.json', 'r', encoding='utf-8-sig').read()))

    fg_layer_one=folium.FeatureGroup(name="MapBox Bright")
    fg_layer_one.add_child(folium.TileLayer('MapBox Bright'))

    fg_layer_two=folium.FeatureGroup(name="Mapbox Control Room")
    fg_layer_one.add_child(folium.TileLayer('Mapbox Control Room'))

    map.add_child(fg_name)
    map.add_child(fg_poligon)
    map.add_child(fg_layer_one)
    map.add_child(folium.LayerControl())
    path='./data/map/index.html'
    map.save(path)

if __name__ == '__main__':
    main()
