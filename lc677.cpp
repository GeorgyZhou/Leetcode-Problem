class MapSum {
public:
    /** Initialize your data structure here. */
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        if (strs.find(key) != strs.end()) val = val - container[key];
        strs.insert(key);
        for (int i = 1; i <= key.size(); i++) {
            string prefix = key.substr(0, i);
            if (container.find(prefix) != container.end()) {
                container[prefix] += val;
                continue;
            }
            container[prefix] = val;
        }
    }
    
    int sum(string prefix) {
        if (container.find(prefix) != container.end()) return container[prefix];
        return 0;
    }
private:
    map<string, int> container;
    set<string> strs;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */