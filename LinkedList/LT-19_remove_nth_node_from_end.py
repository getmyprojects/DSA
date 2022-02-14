"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Ref: https://www.youtube.com/watch?v=XVuQxVej6y8
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        # difference between left and right to be same as n
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # remove
        left.next = left.next.next
        return dummy.next



