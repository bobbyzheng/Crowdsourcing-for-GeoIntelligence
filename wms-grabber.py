import os
import sys

south = 39.610284
north = 39.624069
east = -104.851413
west = -104.875875

request = 'http://imsortho.cr.usgs.gov:80/wmsconnector/com.esri.wms.Esrimap/USGS_EDC_Ortho_Colorado?'
request += 'version=1.1.1&'
request += 'REQUEST=GetMap&'
request += 'format=image/jpeg&'
request += 'layers=DenverCO_0.328m_Color_Apr_2006_03&'
request += 'SRS=EPSG:4326&'
request += 'width=800&'
request += 'height=800&'

dy = (north-south)/15;
dx = (east-west)/15;

f = open('urls.txt', 'w')
for i in range(0,15):
	for j in range(0,15):
		url = request
		tmp_west = i*dx
		tmp_east = (i+1)*dx
		tmp_south = j*dy
		tmp_north = (j+1)*dx
		url += 'BBOX='+str(tmp_west+west)+','+str(tmp_south+south)+','+str(tmp_east+west)+','+str(tmp_north+south)
		f.write(url+'\n')
f.close()


