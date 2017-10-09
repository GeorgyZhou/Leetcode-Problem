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
    TreeNode* str2tree(string s) {
        if (s.size() == 0) return NULL;
        if (s.find('(') == string::npos) return new TreeNode(stoi(s));
        TreeNode* curNode;
        int cur;
        bool left = false;
        bool isFirst = true;
        vector<string> children;
        stack<char> st;
        int start;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                if (st.empty()) {
                    start = i+1;
                    if (isFirst) {
                        curNode = new TreeNode(stoi(s.substr(0, i)));
                        isFirst = false;
                    }
                }
                st.push('(');
            } else if (s[i] == ')') {
                st.pop();
                if (st.empty()) {
                    if (left) { 
                        curNode->right = str2tree(s.substr(start, i-start));
                    } else {
                        left = true;
                        curNode->left = str2tree(s.substr(start, i-start));
                    }
                }
            }
        }
        return curNode;
    }
};