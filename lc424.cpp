class Solution {
public:
    int characterReplacement(string s, int k) {
        int start = 0, maxLength = 0, maxCount = 0;
        int count[26] = {0};
        for (int end = 0; end < s.size(); end++) {
            maxCount = max(maxCount, ++count[s[end] - 'A']);
            while (end - start + 1 - maxCount > k) {
                count[s[start] - 'A']--;
                maxCount = 0;
                for (int i = 0; i < 26; i++){
                    if (count[i] > maxCount){
                        maxCount = count[i];
                    }
                }
                start++;
            }
            maxLength = max(maxLength, end - start + 1);
        }
        return maxLength;
    }
};