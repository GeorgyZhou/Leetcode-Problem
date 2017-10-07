class Solution {
public:
    int hammingDistance(int x, int y) {
        int num = x ^ y;
        int cnt = 0;
        while (num != 0) {
            if (num % 2 == 1) cnt++;
            num >>= 1;
        }
        return cnt;
    }
};