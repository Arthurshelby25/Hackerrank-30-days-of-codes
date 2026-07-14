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
print ("Bienvenido al sistema de facturacion")

print ("Ingrese el producto deseado")


def solve(costo_comida, propina, impuestos):
  # Calculate tip and tax values
    propina = costo_comida * (propina/100)
    impuestos = costo_comida * (impuestos/100)
    
    # Sum everything to get the total cost
    costo_total = costo_comida + propina + impuestos
    
    # Print the total cost rounded to the nearest integer
    print(round(costo_total))

if __name__ == '__main__':
    costo_comida = float(input("Digite el precio de la comida").strip())

    propina = int(input("Digite el monto de la propina").strip())

    impuestos = int(input("Digite el monto del impuesto").strip())

    solve(costo_comida, propina, impuestos)