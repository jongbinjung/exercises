#!/usr/bin/env python3
"""
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Created: 2023-04-24
Author: jongbin.jung

Completed on Mon, 24 Apr 2023, 19:12

"""

N = 100


def brute_force(n=N):
    """Just loop"""
    s = 0  # Sum
    s2 = 0  # Sum of squares
    for x in range(1, n + 1):
        s += x
        s2 += x**2
    return s**2 - s2


def analytical(n=N):
    """Analytical closed-form?"""
    s = n * (n + 1) / 2
    s2 = n * (2 * n + 1) * (n + 1) / 6
    return s**2 - s2


def main():
    """Main function"""
    ans_bf = brute_force(N)
    ans = analytical(N)
    assert ans_bf == ans
    print(ans)


if __name__ == "__main__":
    main()
