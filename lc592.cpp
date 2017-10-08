class Solution {
public:
    string fractionAddition(string expression) {
        int A = 0, B = 1, a, b;
        istringstream ss(expression);
        char _;
        while (ss >> a >> _ >> b) {
            A = a * B + b * A;
            B *= b;
            int cd = abs(gcd(A, B));
            A /= cd;
            B /= cd;
        }
        return to_string(A) + "/" + to_string(B);
    }
private:
    int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
};