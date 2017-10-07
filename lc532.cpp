class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) return 0;
        unordered_map<int, int> numbers;
        int cnt = 0;
        for (int i = 0; i < nums.size(); i++) {
            if(numbers.find(nums[i]) == numbers.end()) numbers[nums[i]] = 0;
            numbers[nums[i]]++;
        }
        if (k == 0) {
            for (auto it = numbers.begin(); it != numbers.end(); it++) {
                if (it->second > 1) cnt++;
            }
            return cnt;
        } 
        for (auto it = numbers.begin(); it != numbers.end(); it++) {
            if (numbers.find(it->first - k) != numbers.end()) cnt++;
        }
        return cnt;
    }
};