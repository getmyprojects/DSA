"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Ex:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Note: leetcode 238
"""


class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        # get prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # get postfix and multiply
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    nums = [1,2,3,4]
    obj = Solution()
    res = obj.productExceptSelf(nums)
    print(res)