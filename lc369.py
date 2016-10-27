# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        carry = self.checkCarry(head)
        if carry == 1:
            nh = ListNode(carry)
            nh.next = head
            return nh
        else:
            return head
    
    def checkCarry(self, head):
        if not head.next:
            ret = (head.val + 1) / 10
            head.val = (head.val + 1) % 10
            return ret
        else:
            carry = self.checkCarry(head.next)
            ret = (head.val + carry) / 10
            head.val = (head.val + carry) % 10
            return ret