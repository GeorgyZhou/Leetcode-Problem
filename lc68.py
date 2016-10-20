class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0 or maxWidth == 0:
            return [""]
        line = []
        count = 0
        lines = []
        for word in words:
            n = len(line)
            if count + n + len(word) <= maxWidth:
                count += len(word)
                line.append(word)
            elif n > 1:
                realline = []
                margin = (maxWidth - count) / (n-1)
                residue = (maxWidth - count) % (n-1)
                for w in line:
                    split = (' ' * margin) if residue == 0 else  (' ' * (margin + 1))
                    if residue > 0:
                        residue -= 1
                    realline.append(w)
                    realline.append(split)
                del realline[-1]
                lines.append(''.join(realline))
                line = [word]
                count = len(word)
            elif n == 1:
                realline = []
                realline.append(line[0])
                realline.append(' ' * (maxWidth - count))
                lines.append(''.join(realline))
                line = [word]
                count = len(word)
        realline = []
        for word in line:
            realline.append(word)
            realline.append(' ')
        if count + len(line) > maxWidth:
            del realline[-1]
        else:
            realline.append(' ' * (maxWidth - count - len(line)))
        lines.append(''.join(realline))
        return lines
                