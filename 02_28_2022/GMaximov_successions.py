#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XD."""
import math
import sys
import numpy as np


if __name__ == '__main__':
    S = list()
    SP = list()
    a = 1.

    for i in np.arange(1, 11, 1):
        a = math.pow(10., -i)
        S.append(5 + a)
        SP.append('5 + ' + "\\" + 'frac{1}{10^{' + f'{i}' + '}}')

    print(S)
    print(SP)

    sys.exit(0)
