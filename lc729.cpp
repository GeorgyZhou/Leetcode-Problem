class MyCalendar {
public:
    MyCalendar() {
        
    }
    
    bool book(int start, int end) {
        int startLast = findSmaller(start, false);
        int endLast = findSmaller(end, true);
        // cout << start << "-"  << end <<  ": " << startLast << " " << endLast << endl;
        if (startLast == endLast && (startLast == -1 || calendar[startLast].second == 1)) {
            calendar.insert(calendar.begin() + endLast + 1, {end, 1});
            calendar.insert(calendar.begin() + startLast + 1, {start, 0});
            return true;
        }
        return false;
    }
private:
    vector<pair<int, int>> calendar;
    int findSmaller(int val, bool isEnd) {
        int lo = 0, hi = calendar.size() - 1, mid;
        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if ((isEnd && calendar[mid].first >= val) || (!isEnd && calendar[mid].first > val)) {
                hi = mid - 1;
            } else if (calendar[mid].first <= val) {
                lo = mid + 1;
            }
        }
        return hi;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.book(start,end);
 */