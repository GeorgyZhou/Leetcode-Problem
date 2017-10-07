class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = digitSquare(slow);
            fast = digitSquare(digitSquare(fast));
        } while (slow != fast);
        return slow == 1;
    }
private:
    int digitSquare(int n) {
        int sum = 0, digit;
        while (n != 0) {
            digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
};