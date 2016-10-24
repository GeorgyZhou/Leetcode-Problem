class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.roots = dict()
        size = dict()
        for num in nums:
            if num in self.roots:
                continue
            if self.roots.has_key(num-1) and self.roots.has_key(num+1):
                lr = self.findRoot(num-1)
                rr = self.findRoot(num+1)
                if size[lr] <= size[rr]:
                    size[rr] += (size[lr] + 1)
                    del size[lr]
                    self.roots[lr] = rr
                    self.roots[num] = rr
                else:
                    size[lr] += (size[rr] + 1)
                    del size[rr]
                    self.roots[rr] = lr
                    self.roots[num] = lr
            elif self.roots.has_key(num-1):
                r = self.findRoot(num-1)
                self.roots[num] = r
                size[r] += 1
            elif self.roots.has_key(num+1):
                r = self.findRoot(num+1)
                self.roots[num] = r
                size[r] += 1
            else:
                self.roots[num] = None
                size[num] = 1
        maxsize = 0
        for key in size.keys():
            maxsize = max(size[key], maxsize)
        return maxsize
            
    
    def findRoot(self, key):
        while self.roots.get(key, None) is not None:
            key = self.roots.get(key)
        return key