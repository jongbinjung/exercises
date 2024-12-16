#!/usr/bin/env python3
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Created: 2023-04-12
Author: jongbin.jung

Completed on Wed, 12 Apr 2023, 17:33

"""
import math


def msum(bound, step):
    """Sum of multiples of `step` for integers below `bound`"""
    n = math.floor((bound - 1) / step)
    return (step + (step * n)) * n / 2


def main():
    """Main function"""
    threes = msum(1000, 3)
    fives = msum(1000, 5)
    fifteens = msum(1000, 15)
    print(threes + fives - fifteens)


if __name__ == "__main__":
    main()
