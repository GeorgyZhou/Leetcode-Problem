# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        rp = res
        lp1, lp2 = l1, l2
        while lp1 and lp2:
            if lp1.val >= lp2.val:
                rp.next = lp2
                lp2 = lp2.next
            else:
                rp.next = lp1
                lp1 = lp1.next
            rp = rp.next
        if not lp1:
            rp.next = lp2
        if not lp2:
            rp.next = lp1
        return res.next