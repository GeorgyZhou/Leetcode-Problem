# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            p = random.randint(1, count)
            if p == 1:
                current = cur_node
            cur_node = cur_node.next
        return current.val
