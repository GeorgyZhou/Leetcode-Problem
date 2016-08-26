class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in xrange(len(candidates)):
            if candidates[i] < target:
                for res in Solution.combinationSum(self, candidates, target - candidates[i], i + 1):
                    res.append(candidates[i])
                    res.sort()
                    if res not in ret:
                        ret.append(res)
            elif candidates[i] == target and [candidates[i]] not in ret:
                    ret.append([candidates[i]])
        return ret

    def combinationSum(self, candidates, target, start):
        ret = []
        for i in xrange(start, len(candidates), 1):
            if candidates[i] < target:
                for res in Solution.combinationSum(self, candidates, target - candidates[i], i + 1):
                    res.append(candidates[i])
                    ret.append(res)
            elif candidates[i] == target:
                ret.append([candidates[i]])
        return ret

solution = Solution()
print solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
