class Solution {
public:
    vector<string> wordsAbbreviation(vector<string>& dict) {
        vector<string> res;
        unordered_map<string, vector<int>> maps;
        for (int i = 0; i < dict.size(); ++i) {
            string word = dict[i];
            res.emplace_back(word.size() > 3 ? (word[0] + to_string(word.size() - 2) + word[word.size() - 1]) : word);
            maps[res.back()].emplace_back(i);
        }
        for (auto it = maps.begin(); it != maps.end(); ++it) {
            if ((it->second).size() > 1) removeDup(res, dict, it->second, 2);
        }
        return res;
    }
private:
    void removeDup(vector<string>& res, vector<string> dict, vector<int>& dups, int preLen) {
        unordered_map<string, vector<int>> maps;
        for (int& index : dups) {
            string word = dict[index];
            string abbr = word.size() > preLen + 2 ? (word.substr(0, preLen) + to_string(word.size() - preLen - 1) + word[word.size() - 1]) : word;
            maps[abbr].emplace_back(index);
            res[index] = abbr;
        }
        for (auto it = maps.begin(); it != maps.end(); ++it) {
            if ((it->second).size() > 1) removeDup(res, dict, it->second, preLen + 1);
        }
    }
};