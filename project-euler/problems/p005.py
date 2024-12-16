#!/usr/bin/env python3
"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Created: 2023-04-19
Author: jongbin

Completed on Thu, 20 Apr 2023, 07:13

"""

from typing import Dict, List

from utils import is_prime

N = 20


def factorize(x: int, primes: List[int] = None) -> Dict[int, int]:
    if primes is None:
        primes = [p for p in range(2, N + 1) if is_prime(p)]
    factors = {}
    for p in primes:
        while x % p == 0:
            factors[p] = factors.get(p, 0) + 1
            x /= p
    return factors


def main():
    """Main function"""

    primes = [p for p in range(2, N + 1) if is_prime(p)]

    factors = [factorize(x, primes) for x in range(2, N + 1)]

    lcm_factors = {}
    for f in factors:
        for k, v in f.items():
            lcm_factors[k] = max(lcm_factors.get(k, 0), v)

    ans = 1
    for base, power in lcm_factors.items():
        ans *= base**power

    print(f"{ans:,}")


if __name__ == "__main__":
    main()
