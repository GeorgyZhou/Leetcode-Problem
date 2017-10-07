class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1) return false;
        int sum = 1;
        int i = 2;
        int upper = floor(sqrt(num));
        for (; i <= upper; i++) {
            if (num % i == 0) {
                sum += i;
                if ( i * i != num) {
                    sum += num / i;
                }
                if (sum > num) return false;
            }
        }
        return sum == num;
    }
};