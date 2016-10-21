# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lhead, bhead = None, None
        llast, blast = None, None
        cur = head
        while cur:
            if cur.val < x:
                if llast is None:
                    lhead = cur
                    llast = cur
                    cur = cur.next
                    llast.next = None
                else:
                    llast.next = cur
                    llast = cur
                    cur = cur.next
                    llast.next = None
            else:
                if blast is None:
                    bhead = cur
                    blast = cur
                    cur = cur.next
                    blast.next = None
                else:
                    blast.next = cur
                    blast = cur
                    cur = cur.next
                    blast.next = None
                    
        if lhead is None and bhead is None:
            return None
        elif lhead is None:
            return bhead
        elif bhead is None:
            return lhead
        else:
            cur = lhead
            while cur.next:
                cur = cur.next
            cur.next = bhead
        return lhead