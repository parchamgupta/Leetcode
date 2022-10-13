class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse= True)
        s1 = nums[0]
        for i in range(1, len(nums) - 1):
            s2 = nums[i]
            s3 = nums[i+1]
            if s2 + s3 > s1:
                return s1 + s2 + s3
            s1 = s2
        return 0