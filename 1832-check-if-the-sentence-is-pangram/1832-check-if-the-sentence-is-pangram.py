class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst = [0] * 26
        for c in sentence:
            lst[ord(c) - ord('a')] += 1
            if 0 not in lst:
                return True
        if 0 in lst:
            return False
        return True