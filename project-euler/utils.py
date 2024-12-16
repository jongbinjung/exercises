#!/usr/bin/env python3
"""Shared utilities"""
import math
from typing import Iterator, Dict


def is_prime(x: int) -> bool:
    """Determine whether the integer x is a prime

    Further optimized based on overview for problem 7
    (https://projecteuler.net/overview=0007)

    * 1 is not a prime.
    * All primes except 2 are odd.
    * All primes greater than 3 can be written in the form 6k+/-1.
    * Any number n can have only one primefactor greater than sqrt(n).
    * The consequence for primality testing of a number n is: if we cannot find
      a number f less than or equal sqrt(n) that divides n then n is prime;
      the only primefactor of n is n itself

    """
    if x < 2:
        return False

    if x < 4:
        # 2 and 3 are prime
        return True

    if x & 1 == 0:
        # 2 is the only even prime
        return False

    if x % 3 == 0:
        return False

    # Upper bound of potential prime factors that are not n
    ub = math.floor(math.sqrt(x))

    six_k_minus_one = 5
    while six_k_minus_one <= ub:
        if x % six_k_minus_one == 0:
            return False
        if x % (six_k_minus_one + 2) == 0:
            return False
        six_k_minus_one += 6

    # x must be the only prime factor of x
    return True


def prime_sieve(l: int, u: int) -> Iterator[int]:
    """Use modified sieve to efficiently find primes in some range

    Args:
        l (int): lower bound; inclusive
        u (int): upper bound; exclusive

    Yields:
        Values in [l, u) that are prime

    """
    if l < 0:
        raise ValueError(f"Range must be positive; got [{l}, {u})")
    if l <= 2:
        yield 2
        l = 3
    limit_floor = math.floor(math.sqrt(u))
    if limit_floor & 1 == 0:
        # 2 is the only even prime
        limit_floor += 1
    while not is_prime(l):
        l += 1
    sieve: Dict[int, bool] = {}
    while l < limit_floor:
        if not sieve.get(l, False):
            yield l
        i = 2
        while l * i < u:
            sieve[l * i] = True
            i += 1
        l += 2
    for i in range(limit_floor, u, 2):
        if not sieve.get(i, False):
            yield i


def is_prime_brute_force(x: int) -> bool:
    """Determine whether the integer x is a prime"""
    for a in range(2, x):
        if x % a == 0:
            return False
    return True


if __name__ == "__main__":
    main()
