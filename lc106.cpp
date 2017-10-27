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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        if (n == 0) return NULL;
        return dfs(inorder, postorder, 0, n-1, 0, n-1);
    }

private:
    TreeNode* dfs(vector<int>& inorder, vector<int>& postorder, int start, int end, int ps, int pe) {
        cout << ps << ":" << pe << endl;
        if (ps > pe || start > end) return NULL;
        int rootVal = postorder[pe];
        int i;
        for (i = start; i <= end; i++) {
            if (rootVal == inorder[i]) break;
        }
        cout << i << endl;
        TreeNode* root = new TreeNode(rootVal);
        root->left = dfs(inorder, postorder, start, i-1, ps, ps + i - start - 1);
        root->right = dfs(inorder, postorder, i+1, end, ps + i - start, pe-1);
        return root;
    }
};