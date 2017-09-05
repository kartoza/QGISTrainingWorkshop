#!/usr/bin/env bash

# Usage ./convert_odt.sh path_to_QGIS_folder_in_repo 
# or /bin/bash/convert_odt.sh  path_to_QGIS_folder_in_repo

DATA_PATH=/home/QGISTrainingWorkshop/QGIS

if [ -n "$1" ]
then
    DATA_PATH=$1
fi


for d in $(find ${DATA_PATH} -maxdepth 1 -type d);
    do
    pushd ${d} &&  libreoffice --headless --convert-to pdf *.odt && popd;
done



