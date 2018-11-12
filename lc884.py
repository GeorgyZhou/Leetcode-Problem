class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            s = ""
            for ch in word:
                s += codes[ord(ch) - ord('a')]
            res.add(s)
        print(res)
        return len(res)
