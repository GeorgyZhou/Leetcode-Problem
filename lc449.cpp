/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        return to_string(root->val) + "(" + serialize(root->left) + ")" + "(" + serialize(root->right) + ")";
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") return NULL;
        stack<char> st;
        int val, start;
        TreeNode* node;
        bool isValSet = false, isLeft = true;
        for (int i = 0; i < data.size(); i++) {
            if (data[i] == '(') {
                if (st.empty() && !isValSet) {
                    val = stoi(data.substr(0, i));
                    node = new TreeNode(val);
                    isValSet = true;
                } 
                if (st.empty()) start = i+1;
                st.push(data[i]);
            } else if (data[i] == ')') {
                st.pop();
                if (st.empty()) {
                    if (isLeft) {
                        isLeft = false;
                        node->left = deserialize(data.substr(start, i-start));
                    } else {
                        node->right = deserialize(data.substr(start, i-start));
                    }
                }
            }
        }
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));