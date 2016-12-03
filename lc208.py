class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = ""
        self.dic = dict()
        

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.words = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            if char not in cur.dic:
                cur.dic[char] = TrieNode()
            cur = cur.dic[char]
        cur.word = word
        self.words[word] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.words
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            if char not in cur.dic:
                return False
            cur = cur.dic[char]
        return True        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")