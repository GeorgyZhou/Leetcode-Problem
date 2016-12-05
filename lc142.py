# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        slow = fast = head
        isCircle = False
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                isCircle = True
                break
        if not isCircle:
            return None
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
        