class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        if (n == 0) return {};
        vector<int> res(n, 0);
        vector<int> dp;
        for (int i = n - 1; i >= 0; --i) {
            while (dp.size() > 0 && temperatures[dp.back()] <= temperatures[i]) {
                dp.pop_back();
            }
            res[i] = dp.size() > 0 ? dp.back() - i : 0;
            dp.emplace_back(i);
        }
        return res;
    }
};