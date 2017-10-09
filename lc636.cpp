struct Log {
    int id;
    string status;
    int time;
};

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        vector<Log> times;
        stack<Log> s;
        string fid, status, time;
        for (auto& s : logs) {
            stringstream ss(s);
            getline(ss, fid, ':');
            getline(ss, status, ':');
            getline(ss, time, ':');
            Log item = {stoi(fid), status, stoi(time)};
            times.push_back(item);
        }
        for (Log log : times) {
            if (log.status == "start") {
                s.push(log);
            } else {
                int tmp = log.time - s.top().time + 1;
                res[log.id] += tmp;
                s.pop();
                if (!s.empty()) res[s.top().id] -= tmp;
            }
        }
        return res;
    }
};