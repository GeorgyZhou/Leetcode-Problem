class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        size_t len = dict.size();
        for (int i = 0; i < len; i++) {
            strs.insert(dict[i]);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        int len = word.size();
        for (int i = 0; i < len; i++) {
            const char chr = word[i];
            for (int j = 0; j < 26; j++) {
                if ('a' + j == chr) continue;
                word[i] = 'a' + j;
                if (strs.find(word) != strs.end()) return true;
            }
            word[i] = chr;
        }
        return false;
    }
private:
    set<string> strs;
};