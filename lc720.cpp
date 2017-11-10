class Solution {
public:
    string longestWord(vector<string>& words) {
        unordered_map<string, vector<string>> maps;
        string res;
        for (string word: words) {
            maps[word.substr(0, word.size() - 1)].push_back(word); 
        }
        for (string word: words) {
            if (word.size() == 1)  dfs(word, maps, res);
        } 
        return res;
    }
private:
    void dfs(string word, unordered_map<string, vector<string>>& maps, string& res) {
        if (res.size() == 0 || res.size() < word.size() || (res.size() == word.size() && word < res)) res = word;
        if (maps.find(word) == maps.end()) return;
        for (string newWord: maps[word]) {
            dfs(newWord, maps, res);
        }
    }
};