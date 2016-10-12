# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = None
        head = head
        next = head.next
        while next:
            head.next = prev
            prev = head
            head = next
            next = head.next
        head.next = prev
        return head
        