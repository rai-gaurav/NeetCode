# https://neetcode.io/problems/number-of-one-bits

# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
# You may assume n is a non-negative integer which fits within 32-bits.

# Input: n = 00000000000000000000000000010111
# Output: 4

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # res += 1 if n & 1 else 0
            res += n % 2
            n = n >> 1
        return res
