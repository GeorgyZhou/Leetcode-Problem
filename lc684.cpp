class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        map<int, int> root;
        size_t len = edges.size();
        int x, y, rootX, rootY;
        for (size_t i = 0; i < len; i++){
            auto pair = edges[i];
            x = pair[0];
            y = pair[1];
            if (root.find(x) != root.end() && root.find(y) != root.end()) {
                rootX = findRoot(root, x);
                rootY = findRoot(root, y);
                if (rootX == rootY) return pair;
                root[rootX] = rootY;
            }
            else if (root.find(x) != root.end()) root[y] = findRoot(root, x);
            else if (root.find(y) != root.end()) root[x] = findRoot(root, y);
            else{
                root[x] = y;
                root[y] = y;
            }
        }
    }
private:
    int findRoot(map<int, int> root, int key){
        while (root[key] != key) {
            key = root[key];
        }
        return key;
    }
};