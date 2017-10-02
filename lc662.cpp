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
    int widthOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        int maxWidth = INT_MIN;
        vector<pair<TreeNode*, int>> level(1, make_pair(root, 1));
        vector<pair<TreeNode*, int>> nextLevel;
        while (!level.empty()) {
            int first = -1, last = -1;
            for (int i = 0; i < level.size(); i++) {
                auto pair = level[i];
                TreeNode* node = pair.first;
                int index = pair.second;
                if (first == -1) first = index;
                last = index;
                if (node->left) nextLevel.push_back(make_pair(node->left, index * 2 - 1));
                if (node->right) nextLevel.push_back(make_pair(node->right, index * 2));
            }
            maxWidth = max(maxWidth, last - first + 1);
            level = nextLevel;
            nextLevel.clear();
        }
        return maxWidth;
    }
};