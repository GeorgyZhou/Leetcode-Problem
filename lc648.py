class Solution:
    def replaceWords(self, word_dic, sentence):
        """
        :type word_dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dic = dict()
        for root in word_dic:
            dic[root] = 1
        ret = []
        words = sentence.split(" ")
        for word in words:
            prefix = None
            for j in range(len(word)+1):
                prefix = word[:j]
                if prefix in dic:
                    #ret.append(prefix)
                    break        
            ret.append(prefix)
        return ' '.join(ret).strip(' ')