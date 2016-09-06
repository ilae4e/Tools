import os

import Functions.Networking.update
from Functions.Networking.get_location import Find_Location

Functions.Networking.update.Update(os.path.abspath(Functions.Networking.update.__file__))
results = Find_Location(os.path.abspath(Functions.Networking.update.__file__), "109.64.20.2")
print "City:\t\t\t\t{}\n" \
      "Continent:\t\t\t{}\n" \
      "Country Code:\t\t{}\n" \
      "Country Code 3:\t\t{}\n" \
      "Country Name:\t\t{}\n" \
      "Latitude:\t\t\t{}\n" \
      "Longitude:\t\t\t{}\n" \
      "postal Code:\t\t{}\n" \
      "Region Code:\t\t{}\n" \
      "Time Zone:\t\t\t{}".format(
    results["city"], results["continent"], results["country_code"], results["country_code3"], results["country_name"],
    results["latitude"], results["longitude"], results["postal_code"], results["region_code"], results["time_zone"])
