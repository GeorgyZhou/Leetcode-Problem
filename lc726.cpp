class Solution {
public:
    string countOfAtoms(string formula) {
        int index = 0;
        string ret = "";
        map<string, int> res = rec(formula, index);
        for (map<string, int>::iterator it = res.begin(); it != res.end(); ++it) {
            ret += it->first + (it->second > 1 ? to_string(it->second) : "");
        }
        return ret;
    }
private:
    map<string, int> rec(string s, int& index) {
        int n = s.size();
        map<string, int> res;
        int count = 0;
        while (index < n) {
            if (s[index] == ')') {
                ++index;
                return res;
            } else if (s[index] == '(') {
                ++index;
                map<string, int> subRes = rec(s, index);
                while(index < n && '0' <= s[index] && s[index] <= '9') count = count * 10 + s[index++] - '0';
                for (auto const& entry: subRes) {
                    if (res.find(entry.first) == res.end()) res[entry.first] = 0;
                    res[entry.first] += entry.second * max(count, 1);
                }
                count = 0;
            } else {
                string cur;
                stringstream ss;
                // cout << index << endl;
                if (index < n && 'A' <= s[index] && s[index] <= 'Z') {
                    ss << s[index++];
                }
                while(index < n && 'a' <= s[index] && s[index] <= 'z') ss << s[index++];
                while(index < n && '0' <= s[index] && s[index] <= '9') count = count * 10 + s[index++] - '0';
                if (ss >> cur) {
                    if (res.find(cur) == res.end()) res[cur] = 0;
                    res[cur] += max(count, 1);
                }
                count = 0;
            }
        }
        return res;
        
    }
};