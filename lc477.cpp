class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int dis = 0, cnt, num, n = nums.size();
        for (int i = 0, j; i < 32; i++) {
            cnt = 0;
            for (j = 0; j < n; j++) {
                num = nums[j] >> i;
                if (num % 2 == 1) cnt += 1;
            }
            dis += cnt * (n - cnt);
        }
        return dis;
    }
};