# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l, cur = 0, head
        while cur is not None:
            cur = cur.next
            l += 1
        if l <= 1:
            return head
        k %= l
        if k == 0:
            return head
        count = 0
        cur = head
        while cur is not None:
            count += 1
            if count == l - k:
                newhead = cur.next
                cur.next = None
                iter = newhead
                while iter.next is not None:
                    iter = iter.next
                iter.next = head
                return newhead
            cur = cur.next