class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in candidates:
            if i < target:
                for ans in Solution.combinationSum(self, candidates, target-i):
                    ans.append(i)
                    ans = sorted(ans)
                    if ans not in ret:
                        ret.append(ans)
            elif i == target:
                ret.append([i])
        return ret

solution = Solution()
print solution.combinationSum([2, 1,3,4], 4)
