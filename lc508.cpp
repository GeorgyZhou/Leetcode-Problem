/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        if (!root) return {};
        unordered_map<int, int> sums;
        dfs(root, sums);
        int freq = 0;
        vector<int> ret;
        for (auto& it : sums) {
            if (it.second < freq) continue;
            if (it.second == freq) ret.push_back(it.first);
            if (it.second > freq) {
                freq = it.second;
                ret.clear();
                ret.push_back(it.first);
            }
        }
        return ret;
    }
private:
    int dfs(TreeNode* node, unordered_map<int, int>& sums) {
        int leftVal = 0, rightVal = 0;
        if (node->left) leftVal = dfs(node->left, sums);
        if (node->right) rightVal = dfs(node->right, sums);
        int sum = leftVal + node->val + rightVal;
        if (sums.find(sum) == sums.end()) sums[sum] = 0;
        sums[sum]++;
        return sum;
    }
};