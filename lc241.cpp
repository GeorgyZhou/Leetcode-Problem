class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> oprs;
        vector<char> ops;
        int num = 0;
        for (int i = 0; i < input.size(); i++) {
            if (input[i] == '-' || input[i] == '+' || input[i] == '*') {
                oprs.push_back(num);
                ops.push_back(input[i]);
                num = 0;
            } else {
                num = num * 10 + (input[i] - '0');
            }
        }
        oprs.push_back(num);
        int n = oprs.size();
        return dfs(oprs, ops, 0, n - 1);
    }
private:
    vector<int> dfs(vector<int>& oprs, vector<char>& ops, int start, int end) {
        if (start == end) return {oprs[start]};
        vector<int> ret;
        for (int i = start; i < end; i++) {
            auto left = dfs(oprs, ops, start, i);
            auto right = dfs(oprs, ops, i+1, end);
            for (int& x : left) {
                for (int& y : right) {
                    if (ops[i] == '-') 
                        ret.push_back(x - y);
                    if (ops[i] == '+')
                        ret.push_back(x + y);
                    if (ops[i] == '*')
                        ret.push_back(x * y);
                }
            }
        }
        return ret;
    }
};