#!/usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Created: 2023-04-19
Author: jongbin.jung

Completed on Thu, 20 Apr 2023, 19:51

"""
from functools import reduce
from typing import Dict

from utils import is_prime

TARGET_NUMBER = 600851475143


def next_prime(x: int) -> int:
    """Get the smallest prime number that is greater than x"""
    i = x + 1
    while not is_prime(i):
        i += 1
    return i


def factorize(x: int) -> Dict[int, int]:
    factors = {}
    # Start with prime factor 2
    print("Start")
    p = 2
    while x / p != 1:
        while x % p == 0:
            print(f"Factorizing to {p}")
            factors[p] = factors.get(p, 0) + 1
            x /= p
            print(f"new x = {x}")
        p = next_prime(p)
    # Last factor OBOB
    factors[p] = factors.get(p, 0) + 1
    return factors


def main():
    """Main function"""

    # Brute-force prime factorization
    f = factorize(TARGET_NUMBER)

    # Check answer
    assert reduce(lambda x, y: x * y, f.keys()) == TARGET_NUMBER

    ans = max(f.keys())
    print(f"{ans}")


if __name__ == "__main__":
    main()
