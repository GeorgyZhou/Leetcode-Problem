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
    TreeNode* convertBST(TreeNode* root) {
        if (!root) return root;
        inOrder(root, 0);
        return root;
    }
private:
    int inOrder(TreeNode* node, int sum) {
        int rightVal = 0, leftVal = 0;
        if (node->right) rightVal = inOrder(node->right, sum);
        if (node->left) leftVal = inOrder(node->left, sum + node->val + rightVal);
        int ret = leftVal + rightVal + node->val;
        node->val += rightVal + sum;
        return ret;
    }
};