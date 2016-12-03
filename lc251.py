class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.x = 0
        self.y = -1

    def next(self):
        """
        :rtype: int
        """
        return self.vec2d[self.x][self.y]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self.y += 1
        while self.x < len(self.vec2d) and self.y >= len(self.vec2d[self.x]):
            self.x += 1
            self.y = 0
        return self.x < len(self.vec2d)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())