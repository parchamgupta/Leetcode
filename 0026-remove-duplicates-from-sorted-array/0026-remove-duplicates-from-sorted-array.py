class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        temp = nums[pos]
        for i in range(1, n):
            if nums[i] != temp:
                pos += 1
                nums[i], nums[pos] = nums[pos], nums[i]                
                temp = nums[pos]
        return pos + 1
                
            