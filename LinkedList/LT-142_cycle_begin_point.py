"""
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        meet = self.hasCycle(head)
        if not meet:
            return None

        start = head
        while start != meet:
            start = start.next
            meet = meet.next
        return start

    def hasCycle(self, head):
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow
        return None
