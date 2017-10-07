class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int lastEnd = 0;
        bool isFirst = true;
        int pTime = 0;
        for (int& time : timeSeries) {
            if (isFirst || time > lastEnd) {
                lastEnd = time + duration - 1;
                isFirst = false;
                pTime += duration;
                continue;
            }
            pTime += duration - (lastEnd - time + 1);
            lastEnd = time + duration - 1;
        }
        return pTime;
    }
};