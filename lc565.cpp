class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        unordered_set<int> sets;
        int res = 0;
        for (int& num : nums) {
            if (sets.find(num) != sets.end()) continue;
            res = max(dfs(nums, sets, num, 0), res);
        }
        return res;
    }
    
private:
    int dfs(vector<int>& nums, unordered_set<int> sets, int num, int count) {
        if (sets.find(num) != sets.end()) return count;
        sets.insert(num);
        return dfs(nums, sets, nums[num], count + 1);
    }
};