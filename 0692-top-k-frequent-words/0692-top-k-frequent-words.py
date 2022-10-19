class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        counts = sorted(counts.items(), key=lambda x: (-x[1],x[0]))
        ans = []
        for key, val in counts:
            ans.append(key)
            k -= 1
            if k == 0:
                break
        return ans
            
        