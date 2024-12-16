#!/usr/bin/env python3
"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

Created: 2023-04-12
Author: jongbin.jung

Completed on Wed, 19 Apr 2023, 18:35

"""

FOUR_MILLION = 4000000


def main():
    """Main function"""

    # Initialize; start from 3rd element, with the first even number (2)
    # accounted for
    i = 2
    ans = 2
    fibs = [1, 2]
    next_fib = 0
    while next_fib < FOUR_MILLION:
        next_fib = fibs[i - 2] + fibs[i - 1]
        fibs.append(next_fib)
        i += 1
        if next_fib & 1:  # bit-wise AND to check even-ness
            continue
        ans += next_fib
    print(ans)


if __name__ == "__main__":
    main()
