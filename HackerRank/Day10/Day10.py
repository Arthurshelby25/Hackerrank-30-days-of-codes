#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # 1. Convert integer to binary string and remove the '0b' prefix
    binary_str = bin(n)[2:]

    # 2. Split the string by '0's to get groups of consecutive '1's
    ones_groups = binary_str.split('0')

    # 3. Find the length of the longest group of '1's
    max_ones = max(len(group) for group in ones_groups)

    print(max_ones)