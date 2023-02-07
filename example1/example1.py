#!/usr/bin/env python3


import sys

import matplotlib.pyplot as plt


def main() -> int:
    """Execute main workflow."""
    plt.plot([0, 1], [0, 1])
    plt.show()

    return 0


if __name__ == '__main__':
    # print('Hola Mundo')
    sys.exit(main())
