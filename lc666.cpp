class Solution {
public:
    int pathSum(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        unordered_map<int, int> numMap;
        int sum = 0, index;
        for (int i = 0; i < nums.size(); i++) {
            index = nums[i] / 100 * 10 + nums[i] / 10 % 10;
            numMap[index] = nums[i];
        }
        dfs(numMap, 0, nums[0], sum);
        return sum;
    }
private:
    void dfs(unordered_map<int, int>& numMap, int curSum, int curNum, int& sum) {
        int level = curNum / 100, pos = curNum / 10 % 10, val = curNum % 10;
        curSum += val;
        int leftChild = (level + 1) * 10 + (pos * 2 - 1);
        int rightChild = leftChild + 1;
        if (numMap.find(leftChild) == numMap.end() && numMap.find(rightChild) == numMap.end()) {
            sum += curSum;
            return;
        }
        if (numMap.find(leftChild) != numMap.end()) {
            dfs(numMap, curSum, numMap[leftChild], sum);
        }
        if (numMap.find(rightChild) != numMap.end()) {
            dfs(numMap, curSum, numMap[rightChild], sum);
        }
    }
};