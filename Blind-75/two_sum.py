"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Ex:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Note: Leetcode 1
"""


class Solution:
    def two_sum(self, nums, target):
        hash_table = {}
        for i in range(len(nums)):
            if target-nums[i] in hash_table:
                return [hash_table[target-nums[i]], i]
            else:
                hash_table[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    res = obj.two_sum(nums, target)
    print(res)
    # ==========
    nums = [3, 2, 4]
    target = 6
    res = obj.two_sum(nums, target)
    print(res)
