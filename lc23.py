# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        row = len(lists)
        if row == 0:
            return None
        col = len(lists)
        if col == 0:
            return None
        import heapq
        heap = []
        for head in lists:
            if head is not None:
                heapq.heappush(heap, (head.val, head))
        flag = True
        ret = None
        while len(heap) > 0:
            val, node = heapq.heappop(heap)
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, node.next))
            if flag:
                ret = node
                lastnode = node
                flag = False
            else:
                 lastnode.next = node
                 lastnode = node
        return ret
        
