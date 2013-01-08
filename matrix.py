import hashlib
import urllib2

site = ("http://map1b.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi?TIME=2013-01-08"
        "&SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=MODIS_Terra_"
        "CorrectedReflectance_TrueColor&STYLE=&TILEMATRIXSET=EPSG4326_250m"
        "&TILEMATRIX=%i&TILEROW=%i&TILECOL=%i&FORMAT=image%%2Fjpeg")

for matrix_num in xrange(8,9):
    for x in xrange(85, 115):
        for y in xrange(260,300):
            handle = urllib2.urlopen(site % (matrix_num, x, y))
            fn = "img/matrix_%i_%i_%i.jpeg" % (matrix_num, x, y)
            try:
                img = handle.read()
                handle.close()
            except:
                next
            if True: #len(img) > 5000:  # Hack, i.e. is it not just black pixels
                with open(fn, "w") as fh:
                    fh.write(img)
                print "done %s" % fn
            else:
                print fn + " empty"

                

            
