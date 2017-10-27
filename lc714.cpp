class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (prices.size() == 0) return 0; 
        int hold = -prices[0], sold = 0; 
        for (int i = 1; i < prices.size(); i++) {
            hold = max(hold, sold - prices[i]);
            sold = max(sold, hold + prices[i] - fee);
        }
        return max(hold, sold);
    }
};