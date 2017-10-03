class Solution {
public:
    int newInteger(int n) {
        int ans = 0, factor = 1;
        while (n != 0) {
            ans += (n % 9) * factor;
            factor *= 10;
            n = n / 9;
        }
        return ans;
    }
};