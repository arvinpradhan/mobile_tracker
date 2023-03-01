import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Your number (including code number): ")

phone = phonenumbers.parse(number)

TIME = timezone.time_zones_for_number(phone)

carrier_identity = carrier.name_for_number(phone, "en")

region = geocoder.description_for_number(phone, "en")
print(phone)
print("Time zone: ", TIME)
print("Carrier: ", carrier_identity)
print("Region: ", region)


