class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        auto coes1 = getCoe(a);
        auto coes2 = getCoe(b);
        int cons = coes1[0] * coes2[0] - coes1[1] * coes2[1];
        int coe = coes1[0] * coes2[1] + coes1[1] * coes2[0];
        return to_string(cons) + "+" + to_string(coe) + "i";
    }
private:
    vector<int> getCoe(string s) {
        int split = s.find('+');
        int cons = stoi(s.substr(0, split));
        int coe = stoi(s.substr(split + 1, s.size() - split - 1));
        return {cons, coe};
    }
};