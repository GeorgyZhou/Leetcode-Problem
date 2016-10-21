# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = None
        cur = head
        while cur:
            if newhead is None:
                newhead = cur
                cur = cur.next
                newhead.next = None
            else:
                ncur = newhead
                last = None
                while ncur and cur.val >= ncur.val:
                    last = ncur
                    ncur = ncur.next
                if last is None:
                    tmp = cur
                    cur = cur.next
                    tmp.next = newhead
                    newhead = tmp
                else:
                    tmp = cur
                    cur = cur.next
                    tmp.next = last.next
                    last.next = tmp
        return newhead