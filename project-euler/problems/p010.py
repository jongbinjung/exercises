#!/usr/bin/env python3
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Created: 2023-08-11
Author: jongbin.jung


"""

from utils import is_prime, prime_sieve

THRESHOLD = int(2e6)


def brute_force():
    s = 0
    for i in range(THRESHOLD):
        if is_prime(i):
            s += i
    print(s)


def sieving():
    """Use modified sieve for better efficiency"""
    s = 0
    for i in prime_sieve(2, THRESHOLD):
        s += i
    print(s)


def main():
    """Main function"""
    brute_force()
    sieving()


if __name__ == "__main__":
    main()
