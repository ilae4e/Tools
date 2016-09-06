import pygeoip
import os

def Find_Location(path,IP):
    gi = pygeoip.GeoIP(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), os.pardir), "Databases"), "geo.dat")))
    return gi.record_by_name(IP)