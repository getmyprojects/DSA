"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(slow.data, fast.data)
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    root = Node(1)
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    root.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n2

    obj = Solution()
    meet = obj.hasCycle(root)
