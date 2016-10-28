class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowA, colA = len(A), len(A[0])
        rowB, colB = len(B), len(B[0])
        res = [[0 for _ in xrange(colB)] for _ in xrange(rowA)]
        rdic = []
        cdic = []
        for i in xrange(rowA):
            flag = False
            for j in xrange(colA):
                if A[i][j] != 0:
                    flag = True
            if flag:    
                rdic.append(i)
        for j in xrange(colB):
            flag = False
            for i in xrange(rowB):
                if B[i][j] != 0:
                    flag = True
            if flag:
                cdic.append(j)
        for i in rdic:
            for j in cdic:
                for k in xrange(rowB):
                    res[i][j] += A[i][k] * B[k][j]
        return res
        