# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        node = dummy
        if k == 1:
            return head
        while node.next:
            for i in range(k, 1, -1):
                for j in range(i):
                    node = node.next
                    if not node:
                        return dummy.next
                if i == k:
                    stop = node.next
                node.next = last.next
                last.next = node
                last = node
            last = node.next
            node = node.next
            node.next = stop
        return dummy.next


