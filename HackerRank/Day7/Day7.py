#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # Invertimos la lista con [::-1] y usamos * para imprimir los elementos separados por espacio
    print(*arr[::-1])

