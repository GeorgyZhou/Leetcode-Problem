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
    string tree2str(TreeNode* t) {
        if (!t) return "";
        if (!t->left && !t->right) return to_string(t->val);
        string leftStr = "", rightStr = "";
        if (t->left) leftStr = tree2str(t->left);
        if (t->right) rightStr = tree2str(t->right);
        string str = to_string(t->val);
        if (t->right) {
            str += "(" + leftStr + ")" + "(" + rightStr + ")";
            return str;
        }
        if (t->left) str += "(" + leftStr + ")";
        return str;
    }
};