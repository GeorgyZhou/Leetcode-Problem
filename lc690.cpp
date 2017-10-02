/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        size_t len = employees.size();
        map<int, vector<int>> empSubMap;
        map<int, int> empImpMap;
        for (int i = 0; i < len; i++) {
            empImpMap[employees[i]->id] = employees[i]->importance;
            empSubMap[employees[i]->id] = employees[i]->subordinates;
        }
        deque<int> dq;
        dq.push_back(id);
        set<int> visited;
        int imps = 0, curId, childId, i;
        while (!dq.empty()) {
            curId = dq.front();
            visited.insert(curId);
            dq.pop_front();
            imps += empImpMap[curId];
            for (i = 0; i < empSubMap[curId].size(); i++) {
                childId = empSubMap[curId][i];
                if (visited.find(childId) != visited.end()) continue;
                dq.push_back(childId);
            }
        }
        return imps;
    }
};