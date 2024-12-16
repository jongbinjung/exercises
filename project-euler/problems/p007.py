#!/usr/bin/env python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

Created: 2023-04-25
Author: jongbin.jung

Completed on Tue, 25 Apr 2023, 19:19

"""

from utils import is_prime


def main():
    """Main function"""

    primes = [2, 3, 5, 7, 11, 13]
    i = max(primes)

    while len(primes) < 10001:
        i += 1
        if is_prime(i):
            primes.append(i)
    print(primes[-1])


if __name__ == "__main__":
    main()
