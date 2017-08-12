class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        import sys
        self.dp = dict()
        a = self.shopping(price, special, needs)
        return a
    
    def shopping(self, price, special, needs):
        if tuple(needs) in self.dp:
            return self.dp[tuple(needs)]
        minimum = sys.maxint
        for spec in special:
            flag = True
            new_needs = []
            actual_cost = 0
            for i in xrange(len(needs)):
                new_needs.append(needs[i] - spec[i])
                actual_cost += spec[i] * price[i]
                if needs[i] < spec[i]:
                    flag = False
                    break
            if actual_cost <= spec[-1]:
                flag = False
            if flag:
                minimum = min(minimum, spec[-1] + self.shopping(price, special, new_needs))
        if minimum == sys.maxint:
            minimum = 0
            for i in range(len(needs)):
                minimum += needs[i] * price[i]
        self.dp[tuple(needs)] = minimum
        return minimum