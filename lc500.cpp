class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<unordered_set<int>> rows = {{'1','2','3','4','5','6','7','8','9','0'},
                                           {'q','w','e','r','t','y','u','i','o','p',
                                            'Q','W','E','R','T','Y','U','I','O','P'},
                                           {'a','s','d','f','g','h','j','k','l','A',
                                            'S','D','F','G','H','J','K','L'},
                                           {'z','x','c','v','b','n','m','Z','X','C',
                                            'V','B','N','M'}};
        int curRow;
        bool flag;
        vector<string> ret;
        for (int j = 0, i, k; j < words.size(); j++ ){
            curRow = -1;
            flag = true;
            for ( k = 0; k < words[j].size(); k++) {
                for (i = 0; i < 4; i++) {
                    if (rows[i].find(words[j][k]) == rows[i].end()) continue;
                    if (curRow != -1 && i != curRow) {
                        flag = false;
                        break;
                    }
                    curRow = i;
                }
                if (!flag) break;
            }
            if (flag) ret.push_back(words[j]);
        }
        return ret;
    }
};