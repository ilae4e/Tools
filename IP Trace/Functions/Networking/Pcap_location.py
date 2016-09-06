import pygeoip
import os


def retGeoStr(path, IP):
    try:
        gi = pygeoip.GeoIP(os.path.abspath(os.path.join(
            os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), "Databases"),
            "geo.dat")))
        rec = gi.record_by_name(IP)
        city = rec["city"]
        country = rec["country_code3"]
        if city != "":
            geoLoc = city + ", " + country
        else:
            geoLoc = country
        return geoLoc
    except:
        return "Unregistered"
