"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, h = i + 1, len(nums) - 1

            while l < h:
                three_sum = nums[i] + nums[l] + nums[h]
                if three_sum > 0:
                    h -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while nums[l] == nums[l - 1] and l < h:
                        l += 1

        return res

