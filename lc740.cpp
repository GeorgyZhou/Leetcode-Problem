class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int, int> count;
        int prev = -1, avoid = 0, used = 0, tmp;
        for (int& num : nums) count[num]++;
        for (auto it = count.begin(); it != count.end(); ++it) {
            tmp = max(avoid, used);
            if (it->first == prev + 1) {
                used = avoid + it->first * it->second;
                avoid = tmp;
            } else {
                used = tmp + it->first * it->second;
                avoid = tmp;
            }
            prev = it->first;
        }
        return max(avoid, used);
    }
};