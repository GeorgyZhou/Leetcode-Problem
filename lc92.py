# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        rlast = end = last = next = None
        reverse = False
        count = 0
        cur = head
        while cur:
            count += 1
            if count == m:
                end = cur
                rlast = last
            if reverse:
                next = cur.next
                cur.next = last
                last = cur
                cur = next
            else:
                last = cur
                cur = cur.next
            if count == m:
                reverse = True
            elif count == n:
                reverse = False
                if rlast is None:
                    head.next = cur
                    return last
                else:
                    rlast.next = last
                    end.next = cur
                    return head
                