# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 06:11:12 2023

@author: lcasado-

El programa spider permitirá extraer todas las imágenes de un sitio web, 
de manera recursiva, proporcionando una url como parámetro. 

Gestionarás las siguientes opciones del programa:
./spider [-rlpS] URL

  • Opción -r : descarga de forma recursiva las imágenes en una URL recibida 
  como parámetro.
  
  • Opción -r -l [N] : indica el nivel profundidad máximo de la descarga 
  recursiva.   En caso de no indicarse, será 5.
  
  • Opción -p [PATH] : indica la ruta donde se guardarán los archivos 
  descargados. En caso de no indicarse, se utilizará ./data/.
  
  El programa descargará por defecto las siguientes extensiones:
  ◦ .jpg/jpeg
  ◦ .png
  ◦ .gif
  ◦ .bmp
"""

import argparse
import pathlib
import validators
import os

import myfunctions

MIN_LEVEL_RECUR = 1
MAX_LEVEL_RECUR = 5

def uniform_resource_locator(url_txt):  
  ok_url = validators.url(url_txt)
  if not ok_url:
    parser.error("Invalid url")
  else:
    return url_txt
  

def recursion_level(argument):
  int_arg = int(argument)
  if MIN_LEVEL_RECUR <= int_arg and int_arg <= MAX_LEVEL_RECUR:
    return int_arg
  else:
    parser.error("Recursivity level not between {} and {}". \
                 format(MIN_LEVEL_RECUR,MAX_LEVEL_RECUR))
  
parser = argparse.ArgumentParser(
  prog='spider',
  description='Extraer todas las imágenes de un sitio web',
  epilog='Este es el final de la ayuda'
  )
parser.add_argument('--recursive','-r', 
                    help='Descarga recursivamente las imágenes.',
                    action='store_true'
                    )

parser.add_argument('--level','-l', 
                    help=f'Nivel máximo de la descarga recursiva. \
                      {MAX_LEVEL_RECUR} niveles por defecto.',
                    type=recursion_level)

parser.add_argument( '--path','-p',
                    help='Ruta para guardar las imágenes.',
                    type=pathlib.Path,
                    default='./data/')

parser.add_argument('url',
                    help='URL de un sitio web al que descargar las imágenes',
                    type=uniform_resource_locator,
                    nargs='+')

#args = parser.parse_args(['-p','~/','https://www.eldebate.com/'])

#args = parser.parse_args(['-r','-l','https://www.eldebate.com/'])
args = parser.parse_args(['https://www.eldebate.com/'])

cwd = os.getcwd()
spiderpath = os.path.join(cwd, args.path)

#Detectar si tengo permiso de escribir en ese directorio

if not args.recursive:
  if args.level is None:
    myfunctions.no_recursive(args.url[0], spiderpath)
  else:
    parser.error("recursitivy level incorrect when no recursivity required")
else:
myfunctions.recursive(args.url[0], spiderpath, args.level)