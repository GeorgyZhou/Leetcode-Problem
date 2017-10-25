class Solution {
public:
    string getHint(string secret, string guess) {
        unordered_map<char, int> dic;
        int bulls = 0, cows = 0;
        for (int i = 0; i < guess.size(); i++) {
            if (guess[i] == secret[i]) {
                ++bulls;
            } else {
                dic[secret[i]]++;
            }
        }
        for (int i = 0; i < guess.size(); i++) {
            if (guess[i] != secret[i] && dic.find(guess[i]) != dic.end() && dic[guess[i]] != 0){
                ++cows;
                dic[guess[i]]--;
            }
        }
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};