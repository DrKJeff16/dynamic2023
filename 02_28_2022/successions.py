#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XD."""
import math
import sys
import numpy as np


if __name__ == '__main__':
    S = list()
    SP = list()
    i = 1.
    a = 1.

    while a:
        a = math.pow(10., -i)
        S.append(5 + a)
        SP.append('${5 + ' + "\\" + 'frac{1}{' + f'{a}' + '}}$')
        i += 1.

    print(S)
    print(SP)

    sys.exit(0)
