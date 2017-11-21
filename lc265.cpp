class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        int k = costs[0].size();
        int prevMin = 0, prevSecMin = 0, prevMinIndex = -1;
        for (int i = 0; i < n; ++i) {
            int curMin = INT_MAX, curSecMin = INT_MAX, curMinIndex = -1;
            for (int j = 0; j < k; ++j) {
                int val = (j == prevMinIndex ? prevSecMin : prevMin) + costs[i][j];
                if (curMinIndex == -1) {
                    curMin = val;
                    curMinIndex = j;
                } else if (val < curMin) {
                    curMinIndex = j;
                    curSecMin = curMin;
                    curMin = val;
                } else if (val < curSecMin) {
                    curSecMin = val;
                }
            }
            prevMin = curMin;
            prevMinIndex = curMinIndex;
            prevSecMin = curSecMin;
        }
        return prevMin;
    }
};