class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (indexToVal.find(val) != indexToVal.end()) return false;
        indexToVal[val] = index.size();
        index.push_back(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (indexToVal.find(val) == indexToVal.end()) return false;
        int last = index.size() - 1;
        int curIndex = indexToVal[val];
        indexToVal[index[last]] = curIndex;
        index[last] ^= index[curIndex];
        index[curIndex] ^= index[last];
        index[last] ^= index[curIndex];
        index.pop_back();
        indexToVal.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return index[rand() % index.size()];    
    }
private:
    unordered_map<int, int> indexToVal;
    vector<int> index;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */