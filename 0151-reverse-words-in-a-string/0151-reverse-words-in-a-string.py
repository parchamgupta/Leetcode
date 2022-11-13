class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst = lst[::-1]
        return " ".join(word for word in lst)