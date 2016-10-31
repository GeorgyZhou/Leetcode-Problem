# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        res = []
        queue = [root]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('#')
        for i in xrange(len(res)-1, -1, -1):
            if res[i] == "#" or res[i] == ',':
                res.pop()
            else:
                break
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data += ","
        root = None
        start = 0
        l = len(data)
        res = []
        last = None
        flag = True
        count = 0
        for i in xrange(l):
            if data[i] == ',':
                cur = data[start:i]
                start = i + 1
                if cur == '#':
                    node = None
                else:
                    node = TreeNode(int(cur))
                if flag:
                    root = node
                    last = 0
                    res.append(node)
                    flag = False
                else:
                    res.append(node)
                    if count == 0:
                        res[last].left = node
                        count += 1
                    else:
                        res[last].right = node
                        count = 0
                        last += 1
                        while last < len(res) and res[last] is None:
                            last += 1
        return root
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))