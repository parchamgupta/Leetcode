from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        n -= 1
        ans = "1"
        
        def get(f):
            s = []
            for g, t in groupby(f):
                s.append(str(len(list(t))) + g)
            return "".join(s)
        
        for _ in range(n):
            ans = get(ans)
        
        return ans
                
            