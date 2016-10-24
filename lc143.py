# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        last = next = None
        while p2.next:
            next = p2.next
            p2.next = last if last else None
            last = p2
            p2 = next
        p2.next = last
        p1 = head
        while p1.next and p2.next:
            next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = next
        