class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.num = dict()

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.num[number] = self.num.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        table = self.num
        j = 0
        for n in table:
            j = value - n
            if j in table and (j != n or table[j] > 1):
                return True
        return False
            
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)