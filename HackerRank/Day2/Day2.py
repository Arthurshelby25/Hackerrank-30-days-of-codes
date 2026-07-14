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
    print("--- Sistema de Facturación: D' Pedro pasteles en hoja ---")
    
    # 1. Pedimos el precio del plato principal
    costo_comida = float(input("Digite el precio del plato principal: ").strip())
    
    # 2. Definimos nuestra lista de 5 extras en el menú
    print("\n--- Agregue 5 extras a su pedido ---")
    menu_extras = ["Queso extra", "Kétchup", "Mayonesa", "Picante", "Bebida"]
    
    # 3. Recorremos la lista preguntando el precio de cada extra y sumándolo al total
    for extra in menu_extras:
        precio_extra = float(input(f"Digite el precio para el extra ({extra}): ").strip())
        costo_comida += precio_extra
        
    print("\n--- Totales y Propinas ---")
    # 4. Pedimos la propina y los impuestos (como porcentajes)
    propina = int(input("Digite el % de la propina: ").strip())
    impuestos = int(input("Digite el % del impuesto: ").strip())
    
    # 5. Llamamos a tu función original con el costo base + todos los extras sumados
    solve(costo_comida, propina, impuestos)