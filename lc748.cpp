class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        unordered_map<char, int> plate;
        string res = "";
        bool flag;
        for (char& chr : licensePlate) {
            if (chr >= 'a' && chr <= 'z') plate[chr]++;
            if (chr >= 'A' && chr <= 'Z') plate[(char)tolower(chr)]++;
        }
        for (string& word : words) {
            if (res != "" && res.size() <= word.size()) continue;
            flag = true;
            unordered_map<char, int> count;
            for (char& chr : word) {
                count[chr]++;
            }
            for (auto it = plate.begin(); it != plate.end(); ++it) {
                if (it->second > count[it->first]) {
                    flag = false;
                    break;
                }
            }
            if (flag) res = word;
        }
        return res;
    }
};