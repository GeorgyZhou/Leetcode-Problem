class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int count[26] = {0};
        for (int i = 0; i < tasks.size(); i++) {
            count[tasks[i] - 'A']++;
        }
        auto cmp = [] (int x, int y) { return x < y; };
        sort(count, count + 26, cmp);
        int maximum = count[25];
        int idles = n * (maximum - 1);
        for (int i = 24; i >= 0; i--) {
            idles -= min(count[i], maximum - 1);
        }
        return idles > 0 ? idles + tasks.size() : tasks.size();
    }
};