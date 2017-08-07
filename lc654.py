# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        index, max_num = self.find_max(nums)
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        return node
        
    
    def find_max(self, nums):
        index, max_num = 0, nums[0]
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                index = i
        return (index, max_num)