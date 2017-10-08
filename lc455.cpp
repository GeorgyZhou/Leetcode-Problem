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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* rl1 = reverse(l1, NULL);
        ListNode* rl2 = reverse(l2, NULL);
        ListNode* head = new ListNode((rl1->val + rl2->val) % 10);
        ListNode* last = head;
        int val, carry = (rl1->val + rl2->val) / 10;
        ListNode* c1 = rl1->next;
        ListNode* c2 = rl2->next;
        while (c1 && c2) {
            val = c1->val + c2->val + carry;
            carry = val / 10;
            val %= 10;
            ListNode* node = new ListNode(val);
            last->next = node;
            last = node;
            c1 = c1->next;
            c2 = c2->next;
        }
        while (c1 || c2) {
            val = (c1 ? c1->val : c2->val) + carry;
            carry = val / 10;
            val %= 10;
            ListNode* node = new ListNode(val);
            last->next = node;
            last = node;
            if (c1) c1 = c1->next;
            if (c2) c2 = c2->next;
        }
        if (carry != 0) {
            ListNode* node = new ListNode(carry);
            last->next = node;
        }
        //cout << endl;
        return reverse(head, NULL);
    }
private:
    ListNode* reverse(ListNode* l, ListNode* last) {
        ListNode* next = l->next;
        l->next = last;
        return next ? reverse(next, l) : l;
    }
};