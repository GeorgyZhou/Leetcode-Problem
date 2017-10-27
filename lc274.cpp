class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int dp[n+1] = {0};
        for (int i = 0; i < n; i++) 
            dp[min(citations[i], n)]++;
        int count = 0;
        for (int i = n; i >= 0; i--) {
            count += dp[i];
            if (count >= i) return i;
        }
        return 0;
    }
};