#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
# Check if the number is odd
    if N % 2 != 0:
        print("Weird")
    else:
        # If it reaches here, the number is definitely even
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
