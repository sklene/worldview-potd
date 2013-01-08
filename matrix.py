import hashlib
import urllib2

site = ("http://map1b.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi?TIME=2013-01-08"
        "&SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=MODIS_Terra_"
        "CorrectedReflectance_TrueColor&STYLE=&TILEMATRIXSET=EPSG4326_250m"
        "&TILEMATRIX=%i&TILEROW=%i&TILECOL=%i&FORMAT=image%%2Fjpeg")

for matrix_num in xrange(5,6):
    for x in xrange(20):
        for y in xrange(20):
            handle = urllib2.urlopen(site % (matrix_num, x, y))
            img = handle.read()
            handle.close()
            if hashlib.md5(img).hexdigest() != \
                    "733091d2386fcedfe5a37f985725d543":

                fn = "matrix_%i_%i_%i.jpeg" % (matrix_num, x, y)
                with open(fn, "w") as fh:
                    fh.write(handle.read())
                print "done %s" % fn
            
