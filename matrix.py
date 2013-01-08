import hashlib
import urllib2
import urllib
from os import system

site = "http://map1b.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi"

params = {
        "TIME": "2013-01-08",
        "SERVICE": "WMTS",
        "REQUEST": "GetTile",
        "VERSION": "1.0.0",
        "LAYER": "MODIS_Terra_CorrectedReflectance_TrueColor",
        "STYLE": None,
        "TILEMATRIXSET": "EPSG4326_250m",
        "FORMAT": "image%2Fjpeg"
        }


australia = {
        8: (85, 120, 260, 300),
#        8: (96, 100, 265, 270),  # Testing settings, just does a 5*5 matrix
        }

zoom = 8
xmin, xmax, ymin, ymax = australia[zoom]

for x in xrange(xmin, xmax + 1):
    for y in xrange(ymin, ymax + 1):
        this_params = params
        this_params["TILEMATRIX"] = zoom
        this_params["TILEROW"] = x
        this_params["TILECOL"] = y
        handle = urllib2.urlopen(site, urllib.urlencode(this_params))
        fn = "img/matrix_%i_%i_%i.jpeg" % (zoom, x, y)
        try:
            img = handle.read()
            handle.close()
        except:
            img = None
        with open(fn, "w") as fh:
            fh.write(img)
        print "done %s" % fn
    # Join the images into a row
    system("convert img/matrix_%i_%i_* +append img/row_%i_%i.jpeg" %
        (zoom, x, zoom, x))

# Make the big image
rows = " ".join(
        ["img/row_%i_%i.jpeg" % (zoom, iii) for iii in xrange(xmin, xmax + 1)]
        )
system("convert %s +append image_%i.png" % (rows, zoom))
