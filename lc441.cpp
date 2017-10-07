class Solution {
public:
    int arrangeCoins(int n) {
        double upper = n * 2.0;
        return floor(-0.5 + sqrt(0.25 + upper));
    }
};