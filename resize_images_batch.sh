#!/usr/bin/env bash
# Purpose: batch image resizer
# Source: https://guides.wp-bullet.com
# Author: Enrico Piazza

# absolute path to image folder
FOLDER=`pwd`

read -p "Are you sure you want to resize all images contained (recursive) in $FOLDER ? " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]
then
    
    # max height
    WIDTH=416

    # max width
    HEIGHT=416

    #resize png or jpg to either height or width, keeps proportions using imagemagick
    #find ${FOLDER} -iname '*.jpg' -o -iname '*.png' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

    #resize png to either height or width, keeps proportions using imagemagick
    #find ${FOLDER} -iname '*.png' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

    #resize jpg only to either height or width, keeps proportions using imagemagick
    find ${FOLDER} -iname '*.jpg' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

    # alternative
    #mogrify -path ${FOLDER} -resize ${WIDTH}x${HEIGHT}% *.png -verbose
fi


