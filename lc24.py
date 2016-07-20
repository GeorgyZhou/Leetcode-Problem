# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy, node = ListNode(0), head
        dummy.next = head
        last = dummy
        while node and node.next:
            if node.next.next:
                tmp = node.next.next
            else:
                tmp = None
            last.next = node.next
            last = node.next.next = node
            node.next = tmp
            node = tmp
        return dummy.next

