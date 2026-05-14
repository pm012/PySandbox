"""
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.
"""
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        
        nums.sort()
        
        expected = list(range(1, n + 1)) + [n]
        
        return nums == expected    
    
class Solution1:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        freq = [0] * (n + 1)

        for x in nums:
            if x < 1 or x > n:
                return False
            freq[x] += 1

        for i in range(1, n):
            if freq[i] != 1:
                return False

        return freq[n] == 2
