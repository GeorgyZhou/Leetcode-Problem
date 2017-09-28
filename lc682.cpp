class Solution {
public:
    int calPoints(vector<string>& ops) {
        size_t len = ops.size();
        int score = 0;
        stack<int> s;
        string op;
        int curScore;
        for (size_t i = 0; i < len; i++) {
            op = ops[i];
            if (op == "C") {
                int lastScore = s.top();
                s.pop();
                curScore = -lastScore;
            }
            else if (op == "+") {
                int lastScore = s.top();
                s.pop();
                int llScore = s.top();
                curScore = lastScore + llScore;
                s.push(lastScore);
                s.push(curScore);
            }
            else if (op == "D") {
                int lastScore = s.top();
                curScore = lastScore * 2;
                s.push(curScore);
            }
            else {
                curScore = stoi(op);
                s.push(curScore);
            }
            cout << curScore << endl;
            score += curScore;
        }
        return score;
    }
};