class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> cache(n, vector<int>(n, -1));
        for (int i = 0; i < n; i++)
            cache[i][i] = nums[i];
        return dfs(nums, 0, n-1, cache) >= 0;
    }
private:
    
    int dfs(vector<int>& nums, int start, int end, vector<vector<int>>& cache) {
        if (cache[start][end] != -1) return cache[start][end];
        int a = nums[start] - dfs(nums, start+1, end, cache);
        int b = nums[end] - dfs(nums, start, end-1, cache);
        cache[start][end] = max(a, b);
        return cache[start][end];
    }
};