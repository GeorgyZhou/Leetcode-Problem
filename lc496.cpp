class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        unordered_map<int, int> dict;
        int n = nums.size();
        stack<int> stk;
        for (int i = 0; i < n; i++) {
            while (!stk.empty() && stk.top() < nums[i]) {
                dict[stk.top()] = nums[i];
                stk.pop();
            }
            stk.push(nums[i]);
        }
        while (!stk.empty()) {
            dict[stk.top()] = -1;
            stk.pop();
        }
        n = findNums.size();
        vector<int> ret;
        for (int i = 0; i < n; i++) {
            ret.push_back(dict[findNums[i]]);
        }
        return ret;
    }
};