# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        head2 = self.findMid(head)
        if head2 is head:
            return True
        head2 = self.reverse(head2)
        cur1, cur2 = head, head2
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        last, cur, next = head, head.next, None
        last.next = None
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        return last
    
    def findMid(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow