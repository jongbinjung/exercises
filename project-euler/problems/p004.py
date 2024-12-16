#!/usr/bin/env python3
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Created: 2023-04-20
Author: jongbin.jung

Completed on Mon, 24 Apr 2023, 19:02

"""


def is_palindrome(s) -> bool:
    """Check whether s is a palindrome"""
    s = str(s)
    for i in range(round(len(s) / 2)):
        if s[i] != s[-(i + 1)]:
            return False
    return True


def brute_force():
    """Just check all three-digit numbers?"""
    ans, ret_x, ret_y = 0, 0, 0
    for x in range(100, 1000):
        for y in range(x, 1000):
            candidate = x * y
            if candidate > ans and is_palindrome(candidate):
                ans = candidate
                ret_x = x
                ret_y = y
    return ans, (ret_x, ret_y)


def main():
    """Main function"""

    ans, xy = brute_force()
    print(f"{xy[0]} * {xy[1]} = {ans}")


if __name__ == "__main__":
    main()
