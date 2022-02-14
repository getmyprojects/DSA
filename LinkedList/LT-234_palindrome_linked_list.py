"""
Given the head of a singly linked list, return true if it is a palindrome.
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True
        mid = self.middle(head)
        last = self.reverse(mid)
        cur = head
        while last:
            if last.val != cur.val:
                return False
            last = last.next
            cur = cur.next

        return True

    def middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev


