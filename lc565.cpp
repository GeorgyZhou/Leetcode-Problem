class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        unordered_set<int> sets;
        int res = 0, count, num;
        for (int i = 0; i < nums.size(); ++i) {
            num = nums[i];
            if (sets.find(num) != sets.end()) continue;
            count = 0;
            while (sets.find(num) == sets.end()) {
                ++count;
                sets.insert(num);
                num = nums[num];
            }
            res = max(res, count);
        }
        return res;
    }
};