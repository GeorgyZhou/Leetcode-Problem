class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        bool isValid;
        int mark, digit;
        for (int num = left; num <= right; ++num) {
            isValid = true;
            mark = 1;
            while (mark <= num) {
                digit = num / mark % 10;
                if (digit == 0 || num % digit != 0) {
                    isValid = false;
                    break;
                }
                mark *= 10;
            }
            if (isValid) res.emplace_back(num);
        }
        return res;
    }
};