class Solution {
public:
    bool hasAlternatingBits(int n) {
        int cur, last = -1;
        while (n != 0) {
            cur = n % 2;
            n /= 2;
            if (cur == last) return false;
            last = cur;
        }
        return true;
    }
};