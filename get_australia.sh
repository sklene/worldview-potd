#!/bin/bash

# Zoom Levels:
zoom=8  # use xmin=85, xmax=115, ymin=260, ymax=300

xmin=85
xmax=115
ymin=260
ymax=300

for x in `seq $xmin $xmax`
do
    for y in `seq $ymin $ymax`
    do
        link="http://map1b.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi?"
        link="${link}TIME=2013-01-08&SERVICE=WMTS&REQUEST=GetTile&VERSION="
        link="${link}1.0.0&LAYER=MODIS_Terra_CorrectedReflectance_TrueColor&"
        link="${link}STYLE=&TILEMATRIXSET=EPSG4326_250m&TILEMATRIX=${zoom}"
        link="${link}&TILEROW=${x}&TILECOL=${y}&FORMAT=image%%2Fjpeg"
        wget "$link" -O "img/matrix_${zoom}_${x}_${y}.jpg"
    done
    convert matrix_${zoom}_${x}_* +append row_${zoom}_${x}.jpg
done
convert row_${zoom}_* -append image_${zoom}.jpg


