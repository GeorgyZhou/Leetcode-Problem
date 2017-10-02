#include<sstream>

class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        stringstream ss;
        int time = 0;
        for (; ss.str().length() < B.length(); ss << A){
            time++;
        }
        if (ss.str().find(B) != std::string::npos) return time;
        ss << A;
        if (ss.str().find(B) != std::string::npos) return time + 1;
        return -1;
    }
};