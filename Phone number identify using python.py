import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


number=input("ENTER THE NUMBER = ")

country = phonenumbers.parse(number, "ch")
print(geocoder.description_for_number(country, "en"))


service_provider = phonenumbers.parse(number, "Ro")
print(carrier.name_for_number(service_provider, "en"))