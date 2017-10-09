class Solution {
public:
    int findMinArrowShots(vector<pair<int, int>>& points) {
        if (points.size() == 0) return 0;
        auto cmp = [](pair<int, int> p1, pair<int, int> p2) {
            return p1.first == p2.first ? p1.second < p2.second : p1.first < p2.first;
        };
        sort(points.begin(), points.end(), cmp);
        int last = points[0].second, cnt = 1;
        for (int i = 1; i < points.size(); i++) {
            last = min(last, points[i].second);
            if (points[i].first > last) {
                last = points[i].second;
                cnt += 1;
            }
        }
        return cnt;
    }
};