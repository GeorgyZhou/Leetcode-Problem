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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode* node = root;
        vector<int> res;
        while (!st.empty() || node) {
            if (node) {
                st.push(node);
                res.push_back(node->val);
                node = node->right;
            } else {
                node = st.top()->left;
                st.pop(); 
            }         
        }
        reverse(res.begin(), res.end());
        return res;
    }
};