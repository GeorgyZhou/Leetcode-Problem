class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string res = to_string(N);
        int marker = res.size();
        for (int i = res.size() - 1; i > 0; --i) {
            if (res[i] < res[i-1]) {
                marker = i;
                res[i-1] = res[i-1] - 1;
            }
        }
        for (int i = marker; i < res.size(); ++i) res[i] = '9';
        return stoi(res);
    }
};