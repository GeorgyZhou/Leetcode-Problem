class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ret = 0
        dic = dict()
        la, lb, lc, ld = len(A), len(B), len(C), len(D)
        for i in range(la):
            for j in range(lb):
                key = A[i] + B[j]
                dic[key] = dic.get(key, 0) + 1
        for i in range(lc):
            for j in range(ld):
                key = C[i] + D[j]
                if -key in dic:
                    ret += dic[-key]
        return ret