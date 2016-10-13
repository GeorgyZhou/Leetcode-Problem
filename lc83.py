# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        last = head
        next = head.next
        while next:
            if next.val == last.val:
                last.next = next.next
            else:
                last = next
            next = next.next
        return head