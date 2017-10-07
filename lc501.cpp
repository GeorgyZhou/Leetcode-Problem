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
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> cnt;
        int maximum = INT_MIN;
        vector<int> ret;
        dfs(root, cnt);
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            if (it->second < maximum) continue;
            if (it->second > maximum) ret.clear();
            ret.push_back(it->first);
            maximum = it->second;
        }
        return ret;
    }
    
private:
    void dfs(TreeNode* node, unordered_map<int, int>& cnt) {
        if (!node) return;
        if (cnt.find(node->val) == cnt.end()) cnt[node->val] = 0;
        cnt[node->val]++;
        dfs(node->left, cnt);
        dfs(node->right, cnt);
    }
};