# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        last, mid = self.findMid(head)
        last.next = None
        ll = self.sortList(head)
        rl = self.sortList(mid)
        ret = self.merge(ll, rl)
        return ret
        
    def findMid(self, head):
        fast = slow = head
        last = None
        while fast and fast.next:
            fast = fast.next.next
            last = slow
            slow = slow.next
        return last, slow
    
    def merge(self, ll , rl):
        newhead = last = None
        lc, rc = ll, rl
        while lc and rc:
            if lc.val <= rc.val:
                if last is None:
                    last = lc
                    newhead = lc
                else:
                    last.next = lc
                    last = lc
                lc = lc.next
            else:
                if last is None:
                    last = rc
                    newhead = rc
                else:
                    last.next = rc
                    last = rc
                rc = rc.next
        if lc:
            last.next = lc
        if rc:
            last.next = rc
        return newhead
        