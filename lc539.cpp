class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> mins;
        for (int i = 0; i < timePoints.size(); i++) {
            mins.push_back(toMinute(timePoints[i]));
        }
        sort(mins.begin(), mins.end(), less<int>());
        int diff = 24 * 60, tmp;
        int s = mins.size();
        int mod = 24 *60;
        for (int i = 0; i < mins.size(); i++) {
            tmp = (mins[i] - mins[((i-1) % s + s) % s]);
            tmp = tmp < 0 ? (mod + tmp) : tmp;
            diff = min(tmp, diff);
        }
        return diff;
    }
private:
    int toMinute (string s) {
        int res;
        res = stoi(s.substr(0, 2)) * 60 + stoi(s.substr(3,2));
        return res;
    }
};