class Solution {
public:
    int evaluate(string expression) {
        unordered_map<string, int> variables;
        return evaluate(expression, variables);
    }
private:
    int evaluate(string expr, unordered_map<string, int> vars) {
        if (expr[0] == '-' || (expr[0] >= '0' && expr[0] <= '9')) return stoi(expr);
        if (expr[0] != '(') return vars[expr];
        string exp = expr.substr(1, expr.size() - 2);
        int start = 0;
        string word = parseExpr(exp, start);
        if (word == "let") {
            while (true) {
                string var = parseExpr(exp, start);
                if (start > exp.size()) return evaluate(var, vars);
                string val = parseExpr(exp, start);
                vars[var] = evaluate(val, vars);
            }
        } else if (word == "add") {
            return evaluate(parseExpr(exp, start), vars) + evaluate(parseExpr(exp, start), vars);
        } else if (word == "mult") {
            return evaluate(parseExpr(exp, start), vars) * evaluate(parseExpr(exp, start), vars);
        }
    }
    
    string parseExpr(string& expr, int& start) {
        int end = start+1, tmp = start, count = 1;
        if (expr[start] == '(') {
            while (count != 0) {
                if (expr[end] == '(') {
                    ++count;
                } else if (expr[end] == ')') {
                    --count;
                }
                ++end;
            }
        } else {
            while (end < expr.size() && expr[end] != ' ') ++end;
        }
        start = end + 1;
        return expr.substr(tmp,  end - tmp);
    }
};