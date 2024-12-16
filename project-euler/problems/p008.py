#!/usr/bin/env python3
"""
The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?

Created: 2023-04-26
Author: jongbin.jung

Completed on Wed, 26 Apr 2023, 23:28

"""

from functools import reduce

THE_NUMBER = "".join(
    """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".split()
)

DIGITS = 13


def main():
    """Main function"""

    # Let n be the first number of specified DIGITS (=13)
    # and m be the product of each digit
    n = THE_NUMBER[:DIGITS]
    m = reduce(lambda a, b: a * int(b), n[1:], int(n[0]))
    # Keep track of the largest m and the argument n that gives the result
    largest_m = m
    arg_n = n
    for i in range(DIGITS, len(THE_NUMBER)):
        old_digit = n[0]
        new_digit = THE_NUMBER[i]
        # Construct the next n
        n = n[1:] + new_digit
        # Compute the next m, excluding any zeros
        if old_digit != "0":
            m /= int(old_digit)
        if new_digit != "0":
            m *= int(new_digit)
        # Skip any sequence with a zero
        if "0" in n:
            continue
        # Does this new (non-zero) sequence beat the current winner?
        if m > largest_m:
            largest_m = int(m)
            arg_n = n
    print(f"Product of the digets: {arg_n} = {largest_m}")


if __name__ == "__main__":
    main()
