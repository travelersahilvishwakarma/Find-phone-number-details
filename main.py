import phonenumbers
from phonenumbers import timezone , geocoder , carrier
import opencage
import folium

number = input("Enter number with +__: ")
phone = phonenumbers.parse(number)
print(phone)

time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(time)
print(car)
print(reg)

from opencage.geocoder import OpenCageGeocode 

key = 'e431b2c3bd5643faa07dc8b82031bfc6'
geocoder = OpenCageGeocode(key)
query = str(reg)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry'] ['lat']
long = results[0]['geometry'] ['lng'] 
print (lat, long)

mymap = folium.Map(location = [lat, long], zoom_start= 9)
folium.Marker([lat, long], popup= reg).add_to(mymap)

mymap.save("location.html")