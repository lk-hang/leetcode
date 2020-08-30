"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 1
        copyhead = head
        while copyhead.next:
            n += 1
            copyhead = copyhead.next

        for i in range(n // 2):
            head = head.next

        return head

