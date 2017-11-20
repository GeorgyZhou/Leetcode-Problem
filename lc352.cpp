/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class SummaryRanges {
public:
    /** Initialize your data structure here. */
    SummaryRanges() {

    }

    void addNum(int val) {
        long left = 0, right = vec.size(), mid = -1;
        long index = -1;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (left + 1 == right && vec[left].start < val) {
                index = left;
                break;
            } else if (vec[mid].start == val) {
                index = mid;
                break;
            } else if (val < vec[mid].start) {
                right = mid;
            } else {
                left = mid;
            }
        }
        
        if (index != -1 && vec[index].end >= val) return;
        if (index != vec.size() - 1 && val + 1 == vec[index + 1].start) {
            vec[index + 1].start = val;
        } else if (index != -1 && val - 1 == vec[index].end) {
            vec[index].end = val;
        } else {
            vec.insert(vec.begin() + index + 1, Interval(val, val));
        }
        
        if (index != -1 && index != vec.size() - 1 && vec[index].end + 1  == vec[index+1].start) {
            vec[index].end = vec[index + 1].end;
            vec.erase(vec.begin() + index + 1);
        }
        return;
    }

    vector<Interval> getIntervals() {
        return vec;
    }
private:
    vector<Interval> vec;
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */