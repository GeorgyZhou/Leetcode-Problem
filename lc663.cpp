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
    bool checkEqualTree(TreeNode* root) {
        if (!root) return false;
        vector<int> sums;
        int sum = getSum(root, sums);
        for (int i = 0; i < sums.size() - 1; i++){
            if (sum == sums[i] * 2) return true;
        }
        return false;
    }
private:
    int getSum(TreeNode* node, vector<int>& sums) {
        int leftSum = 0, rightSum = 0;
        if (node->left) leftSum = getSum(node->left, sums);
        if (node->right) rightSum = getSum(node->right, sums);
        int sum = leftSum + rightSum + node->val;
        sums.push_back(sum);
        return sum;
    }
};