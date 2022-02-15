"""
Given the head of a linked list, rotate the list to the right by k places.
Ref: https://www.youtube.com/watch?v=UcGtPs2LE_c
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        # get length and tail
        size, tail = 1, head

        while tail.next:
            size += 1
            tail = tail.next

        k = k % size
        if k == 0:
            return head

        # move to pivot and rotate
        cur = head
        for _ in range(size - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head
