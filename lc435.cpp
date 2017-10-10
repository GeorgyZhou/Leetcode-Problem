/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        auto cmp = [](Interval t1, Interval t2) {
            return t1.start == t2.start ? t1.end < t2.end : t1.start < t2.start; 
        };
        sort(intervals.begin(), intervals.end(), cmp);
        int cnt = 0;
        int end = INT_MIN;
        for (int i = 0; i < intervals.size(); i++) {
            if (intervals[i].start < end) {
                end = min(end, intervals[i].end);
                cnt++;
            } else {
                end = intervals[i].end;
            }
        }
        return cnt;
    }
};