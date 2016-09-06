import mechanize
import os
import gzip

def Update(path):
    br = mechanize.Browser()
    br.open("http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz")


    with open(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), os.pardir), "Databases"), "geo.dat.gz")), "wb") as e:
        results = br.response().read()
        e.write(results)
    with gzip.open(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), os.pardir), "Databases"), "geo.dat.gz")), "rb") as e:
        with open(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), os.pardir), "Databases"), "geo.dat")), "wb") as f:
            f.write(e.read())

    os.remove(os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.normpath(path), os.pardir), os.pardir), os.pardir), "Databases"), "geo.dat.gz")))
