class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        nums.sort()
        for i in range(nums_length - 1):
            if nums[i] == nums[i+1]:
                return True
            

        return False
        