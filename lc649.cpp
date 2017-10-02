class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.length();
        auto cmp = [] (int x, int y) { return x > y; }; 
        priority_queue<int, vector<int>, decltype(cmp)> rQueue(cmp);
        priority_queue<int, vector<int>, decltype(cmp)> dQueue(cmp);
        for (int i = 0; i < senate.length(); i++) {
            if (senate[i] == 'R') rQueue.push(i);
            if (senate[i] == 'D') dQueue.push(i);
        }
        while (!rQueue.empty() && !dQueue.empty()) {
            int ri = rQueue.top(), di = dQueue.top();
            rQueue.pop();
            dQueue.pop();
            if (ri < di) rQueue.push(ri + n);
            if (ri > di) dQueue.push(di + n);
        }
        
        return rQueue.size() > dQueue.size() ? "Radiant" : "Dire";
    }
};