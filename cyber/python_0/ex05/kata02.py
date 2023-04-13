#!/usr/bin/python3

import sys

kata = (2019, 9, 25, 3, 30)
resultado = "{:0>2}/{:0>2}/{:4} {:0>2}:{:0>2}".format(kata[1], kata[2], kata[0], kata[3], kata[4])
print(resultado)
