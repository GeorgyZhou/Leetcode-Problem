class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1) return 9;
        int lower = pow(10, n - 1); 
        int upper = pow(10, n) - 1;
        for (int i = upper; i >= lower; i--) {
            long cand = buildCand(i);
            for (long j = upper; j * j >= cand; j--) {
                if (cand % j == 0 && cand / j <= upper) {
                    return cand % 1337;
                }
            }
        }
    }
private:
    long buildCand(int n) {
        string s = to_string(n);
        reverse(s.begin(), s.end());
        return stol(to_string(n) + s);
    }
};