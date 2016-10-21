# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        last, cur, next, newhead = None, head, None, None
        while cur:
            next = cur.next
            flag = False
            while next and next.val == cur.val:
                flag = True
                cur = next
                next = cur.next
            if not flag:
                if last is None:
                    newhead = cur
                    last = cur
                    last.next = None
                else:
                    last.next = cur
                    last = cur
                    last.next = None
            cur = next
        return newhead
                
        