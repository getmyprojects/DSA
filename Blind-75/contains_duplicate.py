"""
Given an integer array nums, return true if any value appears at least twice in
 the array, and return false if every element is distinct.

Note: leetcode 217
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) > len(set(nums)) else False  # one line solution
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
    