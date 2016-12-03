class LinkListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None  # next key
        self.last = None  # next key

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dic = dict()
        self.head_key = None
        self.tail_key = None

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic or self.cap <= 0:
            return -1
        node = self.dic[key]
        node_last, node_next = node.last, node.next
        if node_last:
            if node_next:
                self.dic[node_next].last = node_last
            else:
                self.tail_key = node_last
            self.dic[node_last].next = node_next
            node.next = self.head_key
            self.dic[self.head_key].last = key
            node.last = None
            self.head_key = key
        return node.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = LinkListNode(value)
        if len(self.dic) == self.cap:
            last = self.dic[self.tail_key].last
            del self.dic[self.tail_key]
            if last:
                self.dic[last].next = None
                self.tail_key = last
            else:
                self.tail_key = None
                self.head_key = None
        self.dic[key] = node
        if self.head_key:
            node.next = self.head_key
            self.dic[self.head_key].last = key
        self.head_key = key
        if self.tail_key is None:
            self.tail_key = key

s = LRUCache(10)
s.set(10,13)
s.set(3,17)
s.set(6,11)
s.set(10,5)
s.set(9,10)
print s.get(13)
s.set(2,19)
print s.get(2)
print s.get(3)
s.set(5,25)
print s.get(8)
s.set(9,22)
s.set(5,5)
s.set(1,30)
print s.get(11)
s.set(9,12)
print s.get(7)
print s.get(5)
print s.get(8)
print s.get(9)
s.set(4,30)
s.set(9,3)
print s.get(9)
print s.get(10)
print s.get(10)
s.set(6,14)
s.set(3,1)
print s.get(3)
s.set(10,11)
print s.get(8)
s.set(2,14)
print s.get(1)
print s.get(5)
print s.get(4)
s.set(11,4)
s.set(12,24)
s.set(5,18)
print s.get(13)
s.set(7,23)
print s.get(8)
print s.get(12)
s.set(3,27)
s.set(2,12)
print s.get(5)
s.set(2,9)
s.set(13,4)
s.set(8,18)
s.set(1,7)
print s.get(6)
s.set(9,29)
s.set(8,21)
print s.get(5)
s.set(6,30)
s.set(1,12)
print s.get(10)
s.set(4,15)
s.set(7,22)
s.set(11,26)
s.set(8,17)
s.set(9,29)
print s.get(5)
s.set(3,4)
s.set(11,30)
print s.get(12)
s.set(4,29)
print s.get(3)
print s.get(9)
print s.get(6)
s.set(3,4)
print s.get(1)
print s.get(10)
s.set(3,29)
s.set(10,28)
s.set(1,20)
s.set(11,13)
print s.get(3)
s.set(3,12)
s.set(3,8)
s.set(10,9)
s.set(3,26)
print s.get(8)
print s.get(7)
print s.get(5)
s.set(13,17)
s.set(2,27)
s.set(11,15)
print s.get(12)
s.set(9,19)
s.set(2,15)
s.set(3,16)
print s.get(1)
s.set(12,17)
s.set(9,1)
s.set(6,19)
print s.get(4)
print s.get(5)
print s.get(5)
s.set(8,1)
s.set(11,7)
s.set(5,2)
s.set(9,28)
print s.get(1)
s.set(2,2)
s.set(7,4)
s.set(4,22)
s.set(7,24)
s.set(9,26)
s.set(13,28)
s.set(11,26)