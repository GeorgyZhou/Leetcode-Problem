class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        bool isComment = false;
        vector<string> res;
        string pureLine;
        for (string& line : source) {
            int i = 0;
            if (!isComment) pureLine = "";
            while (i < line.size()) {
                string s = line.substr(i, 2);
                if (s == "/*" && !isComment) {
                    isComment = true;
                    i += 2;
                } else if (s == "*/" && isComment) {
                    isComment = false;
                    i += 2;
                } else if (s == "//" && !isComment) {
                    break;
                } else {
                    if (!isComment) pureLine += line[i];
                    ++i;
                }
            }
            if (pureLine.size() > 0 && !isComment) res.push_back(pureLine);
        }
        return res;
    }
};