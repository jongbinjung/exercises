#!/usr/bin/env python3
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,


a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

Created: 2023-04-26
Author: jongbin.jung

Completed on Thu, 27 Apr 2023, 00:15

"""

TARGET_SUM = 1000


def main():
    """Main function"""

    squares = [i**2 for i in range(TARGET_SUM)]
    found = False
    for a in range(1, int(TARGET_SUM / 3)):
        a2 = squares[a]
        for b in range(a + 1, int((TARGET_SUM - a) / 2)):
            b2 = squares[b]
            s = a2 + b2
            if s in squares:
                c = squares.index(s)
                if a + b + c == TARGET_SUM:
                    print(f"a={a}, b={b}, c={c}")
                    found = True
                    break
        if found:
            break
    print(a * b * c)


if __name__ == "__main__":
    main()
