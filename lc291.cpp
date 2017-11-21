class Solution {
public:
    bool wordPatternMatch(string pattern, string str) {
        unordered_map<char, string> maps;
        unordered_set<string> str_to_char;
        return dfs(pattern, str, maps, str_to_char, 0, 0);
    }
private:
    bool dfs(string& pattern, string& str, unordered_map<char, string>& maps, unordered_set<string>& str_to_char, int pi, int si) {
        if (pi == pattern.size() && si == str.size()) return true;
        if (pi == pattern.size() || si == str.size()) return false;
        char c = pattern[pi];
        if (maps.find(c) != maps.end()) {
            string sub = maps[c];
            int len = sub.size();
            if (len + si <= str.size() && sub == str.substr(si, len) && 
                dfs(pattern, str, maps, str_to_char, pi + 1, si + len)) {
                return true;
            }
            return false;
        }
        for (int i = 1; i <= str.size() - si; ++i) {
            string ss = str.substr(si, i);
            if (str_to_char.find(ss) != str_to_char.end()) continue;
            str_to_char.insert(ss);
            maps[c] = ss;
            if (dfs(pattern, str, maps, str_to_char, pi + 1, si + i)) return true;
            maps.erase(c);
            str_to_char.erase(ss);
        }
        return false;
    }
};