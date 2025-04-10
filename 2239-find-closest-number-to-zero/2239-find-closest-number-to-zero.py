class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = abs(nums[0])

        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(closest) or (abs(nums[i]) == abs(closest) and nums[i] > closest):
                closest = nums[i]
        
        return closest