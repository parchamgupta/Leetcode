class Solution:
    def countAsterisks(self, s: str) -> int:
        lst = []
        count = 0
        for c in s:
            if c == '*' and len(lst) == 0:
                count += 1
            elif c == '|' and len(lst) == 0:
                lst.append('|')
            elif c == '|' and len(lst) == 1:
                lst.pop()
        return count