class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> cnt;
        int longest = 0, lastNum = -1, lastCnt = 0;
        int curCnt;
        for (int i = 0; i < nums.size(); i++) {
            if (cnt.find(nums[i]) == cnt.end()) cnt[nums[i]] = 0;
            cnt[nums[i]]++;
        }
        for (pair<int, int> p : cnt) {
            if (lastCnt != 0 && lastNum + 1 == p.first) 
                longest = max(longest, p.second + lastCnt);
            lastCnt = p.second;
            lastNum = p.first;
        }
        return longest;
    }
};