#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE costo_comida
#  2. INTEGER propina
#  3. INTEGER impuestos
#

def solve(costo_comida, propina, impuestos):
  # Calculate tip and tax values
    tip = costo_comida * (propina / 100)
    tax = costo_comida * (impuestos / 100)
    
    # Sum everything to get the total cost
    costo_total = costo_comida + tip + tax
    
    # Print the total cost rounded to the nearest integer
    print(round(costo_total))

if __name__ == '__main__':
    costo_comida = float(input().strip())

    propina = int(input().strip())

    impuestos = int(input().strip())

    solve(costo_comida, propina, impuestos)