"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Ex: Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Note: Leetcode 21 for more detail
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_two_lists(l1, l2):
    start = ListNode()
    cur = start

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next

    # edge case in case one list is bigger
    cur.next = l1 or l2
    return start.next


if __name__ == "__main__":
    # list 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    # list 2
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    res = merge_two_lists(l1, l2)
    # print
    while res:
        print(res.val)
        res = res.next