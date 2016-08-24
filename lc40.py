class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        for i in candidates:
            if i < target:

                Solution.combinationSum2(self, candidates.remove(i))