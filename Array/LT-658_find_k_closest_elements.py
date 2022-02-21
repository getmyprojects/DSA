"""
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.

Ref: https://www.youtube.com/watch?v=IRtv7pdp8hQ (using binary search)
Ref: https://www.youtube.com/watch?v=J8yLD-x7fBI (using heap)
"""

# Binary search
class Solution:
    def findClosestElements(self, arr, k, x):
        # idea is to find the left index, and then return left+k from array
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
