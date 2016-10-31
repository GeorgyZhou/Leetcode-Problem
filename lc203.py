# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        newhead, last, cur = None, None, head
        while cur:
            if cur.val == val:
                if newhead:
                    last.next = cur.next
            elif newhead is None:
                newhead = cur
                last = cur
            else:
                last = cur
            cur = cur.next
        return newhead
                    