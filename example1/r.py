#!/usr/bin/env python3
"""Iterating from `x_0` initial value."""


import sys
import numpy as np
import math as m

import matplotlib.pyplot as plt


# def f(x: float, a: float, b: float) -> float:
#     """Dynamic System function."""
#     return (a * x) + b


def f(x: float, r: float) -> float:
    """Quadratic Dynamic System."""
    return x + r - m.pow(x, 2.)


def main() -> int:
    """Execute main workflow."""
    # plt.plot([0, 1], [0, 1])
    # plt.show()

    # Initial Conditions
    X_0 = np.arange(.1, .2, .1)

    for x_0 in X_0:
        # a = 1.
        # a = 2.
        # b = 2.
        # x_0 = .5
        r = 1.  # Periodic Value(?)
        N = 20

        i = np.arange(0, N, 1)
        x = x_0
        X = list()

        for _ in i:
            print(x)
            X.append(x)
            x = f(x, r)

        plt.plot(X)

    # plt.yscale('log')
    plt.show()

    return 0


if __name__ == '__main__':
    # print('Hola Mundo')
    sys.exit(main())
