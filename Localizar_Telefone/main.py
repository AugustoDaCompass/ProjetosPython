import phonenumbers
import opencage
from phone import number
from opencage.geocoder import OpenCageGeocode

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber,"en") ## localizacao do seu numero
print(location)

from phonenumbers import carrier
service = phonenumbers.parse(number)
print(carrier.name_for_number(service, "en")) ## mostra o operadora do seu numero

chave = "sua chave de api do open cage"
geocoder = OpenCageGeocode(chave)
query = str(location)
results = geocoder.geocode(query)
##print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)