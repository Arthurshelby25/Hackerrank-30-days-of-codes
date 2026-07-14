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

print ("Bienvenidos al sistema de facturacion")

def solve (costo_comida, propina, impuestos):
    #calculamos propina e impuestos
    propina = costo_comida * (propina/100)
    impuestos = costo_comida * (impuestos/100)

    #sumar todo para obtener el costo toal 
    costo_total = costo_comida + propina + impuestos 

#imprimir el costo total redondeado
    print(round(costo_total))

costo_comida = float(input("Digite el precio de la comida").strip())
propina = int(input("digite el porcentaje de la propina").strip())
impuestos = int(input("Digite el monto del impuesto").strip())

solve(costo_comida, propina, impuestos)
