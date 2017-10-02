class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        int i = 1, j = k + 1;
        while (i < j) {
            ans.push_back(i++);
            ans.push_back(j--);
        }
        if (i == j) ans.push_back(i);
        for (i = k + 2; i <= n; i++) {
            ans.push_back(i);
        }
        return ans;
    }
};