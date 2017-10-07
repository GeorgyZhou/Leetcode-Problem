class Solution {
public:
    string convertToBase7(int num) {
        bool flag = num < 0;
        if (flag) num = -num;
        int digit, ans = 0, factor = 1;
        while(num) {
            digit = num % 7;
            ans += digit * factor;
            factor *= 10;
            num /= 7;
        }
        if (flag) ans = -ans;
        return to_string(ans);
    }
};