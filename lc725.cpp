/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int n = 0;
        int count = 0;
        vector<ListNode*> res;
        ListNode* node = root;
        while (node) {
            ++n;
            node = node->next;
        }
        int len = n / k, mod = n % k;
        node = root;
        ListNode* lastNode = NULL;
        while (node) {
            if (count == len && mod == 0 || count == len + 1 && mod > 0) {
                count = 0;
                if (mod > 0) --mod;
                if (lastNode) lastNode->next = NULL;
            }
            ++count;
            if (count == 1) res.push_back(node);
            lastNode = node;
            node = node->next;
        }
        while (res.size() < k) res.push_back(NULL);
        return res;
    }
};