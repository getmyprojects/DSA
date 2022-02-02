"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Leetcode 53
"""


class Solution:
    def maxSubArray(self, nums):
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
            
        return max_sub


if __name__ == "__main__":
    obj = Solution()
    res = obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
