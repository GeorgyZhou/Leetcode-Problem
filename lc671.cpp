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
    int findSecondMinimumValue(TreeNode* root) {
        if (!root) return -1;
        int minimum = INT_MAX, secondMin = INT_MAX;
        dfs(root, minimum, secondMin);
        return secondMin == INT_MAX ? -1 : secondMin;
    }
private:
    void dfs(TreeNode* p, int& minimum, int& secondMin) {
        if (p->val < minimum) {
            secondMin = min(minimum, secondMin);
            minimum = p->val;
        }
        else if (p->val != minimum && p->val < secondMin){
            secondMin = p->val;
        }
        if (p->left) dfs(p->left, minimum, secondMin);
        if (p->right) dfs(p->right, minimum, secondMin);
        return;
    }
};