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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return dfs(nums, 0, nums.size()-1);
    }
private:
    TreeNode* dfs(vector<int>& nums, int start, int end) {
        if (start > end) return NULL;
        if (start == end) return new TreeNode(nums[start]);
        int mid = start + (end - start) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = dfs(nums, start, mid-1);
        node->right = dfs(nums, mid+1, end);
        return node;
    }
};