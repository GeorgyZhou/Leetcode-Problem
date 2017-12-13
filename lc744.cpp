class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int distance = INT_MAX;
        char ret;
        for (char& letter: letters) {
            if (letter - target > 0 && letter - target < distance) {
                distance = letter - target;
                ret = letter;
            } else if (letter - target <= 0 && letter - target + 26 < distance) {
                distance = letter -target + 26;
                ret = letter;
            }
        }
        return ret;
    }
};