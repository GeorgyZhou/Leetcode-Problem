class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = []

        for i in xrange(len(candidates)):
            if i == target:
                ret.append([i])
            elif i < target:
                for former in Solution.combinationSum2(self, candidates, target - i):
                    if i not in former:
                        former.append(i)
                        former.sort()
                        if former not in ret:
                            ret.append(former)
        return ret

solution = Solution()
print solution.combinationSum2([1,2,3,5,9],10)