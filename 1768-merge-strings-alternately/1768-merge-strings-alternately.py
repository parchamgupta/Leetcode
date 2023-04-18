class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = ""
        while i in range(len(word1)) and j in range(len(word2)):
            ans += word1[i]
            i += 1
            ans += word2[j]
            j += 1
        if i < len(word1):
            ans += word1[i:]
        if j < len(word2):
            ans += word2[j:]
        return ans