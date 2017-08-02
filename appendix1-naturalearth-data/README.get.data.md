Fetch the data from 

http://www.naturalearthdata.com

Download the 'everything' sqlite from http://www.naturalearthdata.com/downloads/

Unzip the sqlite file to the Appendix-1 folder(that’s where the world.qgs project in Appendix 4 expects it)

Open the terminal(linux) and run the following command:
 ```
  ogr2ogr -f SQLite ne.sqlite name_of_downloaded_sqlite -progress -dsco SPATIALITE=YES -gt 65536 -lco SPATIAL_INDEX=YES
 ```
On windows the above command is run in the OS geo shell. You can find it under Programs and Files >QGIS

Remove the name_of_downloaded_sqlite from natural earth


