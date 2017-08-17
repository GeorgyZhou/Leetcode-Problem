class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        array = [str(i) for i in range(1, n+1)]
        while len(array) != 1:
            new_array = []
            left, right = 0, len(array) - 1
            while left < right:
                new_array.append('(' + array[left] + ',' + array[right] + ')')
                left += 1
                right -= 1
            array = new_array
        return array[0]