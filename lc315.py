class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(enums):
            half = len(enums) / 2
            if not half:
                return enums
            left, right = mergeSort(enums[:half]), mergeSort(enums[half:])
            m, n = len(left), len(right)
            i = j = 0
            while i < m or j < n:
                if j == n or (i < m and left[i][1] <= right[j][1]):
                    enums[i+j] = left[i]
                    ret[left[i][0]] += j
                    i += 1
                else:
                    enums[i+j] = right[j]
                    j += 1
            return enums
        ret = [0 for _ in range(len(nums))]
        mergeSort(list(enumerate(nums)))
        return ret