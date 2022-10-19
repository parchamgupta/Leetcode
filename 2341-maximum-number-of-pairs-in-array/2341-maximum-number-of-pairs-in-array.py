class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        pairs = 0
        solo = 0
        for k, v in counts.items():
            if v % 2 == 0:
                pairs += v // 2
            else:
                pairs += v // 2
                solo += v % 2
        return [pairs, solo]