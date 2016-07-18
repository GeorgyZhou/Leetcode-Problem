
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        first, second = res, res
        for i in xrange(n):
            first = first.next
        while first.next:
            # when first comes to the last one
            # second comes to the n+1 from the end
            first = first.next
            second = second.next
        second.next = second.next.next

        return res.next


