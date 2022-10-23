class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = collections.Counter(nums)
        n = len(nums)
        ans = []
        a = 0
        b = 0
        for i in range(1, n+1):
            if i in temp:
                if temp[i] > 1:
                    a = i
            else:
                b = i
        ans.append(a)
        ans.append(b)
        return ans