#!/usr/bin/python3

"""
Le deuxième programme scorpion recevra des fichiers d’images en tant que 
paramètres et sera capable de les analyser pour en extraire les métadonnées
EXIF et autres, en les affichant à l’écran. 

Le programme sera au moins compatible avec les mêmes extensions que celles 
gérées par spider. Il affichera les attributs de base tels que la date de
création, ainsi que les données EXIF. Le format de sortie dépend de vous.


./scorpion FILE1 [FILE2 ...]
"""
import  exif

import sys

if __name__ == '__main__':
    numarg = len(sys.argv)
    if numarg == 1:
        print(f"Usage is ./scorpion FILE1 [FILE2 ...]")
    else:
        for file in sys.argv[1:]:
            with open(file, 'rb') as image_file:
                my_image = exifImage(image_file)
                if my_image.has_exif:
                    for list in my_image.list_all():
                        print(list)
