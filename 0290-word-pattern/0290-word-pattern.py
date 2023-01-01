class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words):
            return False
        d1 = {}
        d2 = {}
        for ch, word in zip(pattern, words):
            if ch not in d1 and word not in d2:
                d1[ch] = word
                d2[word] = ch
            elif (ch not in d1 and word in d2):
                return False
            elif (ch in d1 and d1[ch] != word):
                return False
        return True
                