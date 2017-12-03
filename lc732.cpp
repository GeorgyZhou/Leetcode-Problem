class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        calendar_book[start]++;
        calendar_book[end]--;
        int res = 0;
        int cur = 0;
        for (auto& p : calendar_book) {
            cur += p.second;
            res = max(res, cur);
        }
        return res;
    }
private:
    map<int, int> calendar_book;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */