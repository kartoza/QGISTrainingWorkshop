"""
This is a small helper file to generate a new set of positional data
for a grid.xml earthquake file. Update the center of the quake below
and then run this file.

Use the first set of numbers to set the bounding box etc. at the top of
the grid.xml.

Use the second output (/tmp/pos) to delete the first two columns in 
matrix section of the grid.xml and replace with new positional data.

The data can then be used with the InaSAFE shakemap importer
to use the grid file with other training data.

Tim Sutton, July 2017
"""
center = [39.23872,-6.79730]
inc = 0.025
count = 161
print center
lon_min=center[0] - ((count/2) * inc)
lat_min=center[1] - ((count/2) * inc)
lon_max=center[0] + ((count/2) * inc)
lat_max=center[1] + ((count/2) * inc)
print lon_min, lat_min
print lon_max, lat_max
out = open('/tmp/pos', 'wt')
for lat in xrange(0,count):
    for lon in xrange(0,count):
       out.write('%.5f %.5f \n' % (lon_min + (inc * lon), lat_min + (inc * lat)))
