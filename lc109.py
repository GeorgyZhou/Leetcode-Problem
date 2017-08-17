# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.buildTree(array, 0, len(array)-1)
        
    def buildTree(self, array, start, end):
        if start > end:
            return None
        medium = (start + end) / 2
        root = TreeNode(array[medium])
        root.left = self.buildTree(array, start, medium-1)
        root.right = self.buildTree(array, medium+1, end)
        return root