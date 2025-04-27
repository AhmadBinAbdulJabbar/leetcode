class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        num = set(nums)
        max_length = 1
        for n in num:
            if (n-1) not in num:
                curr_len = 0
                while (n+curr_len) in num:
                    curr_len +=1
                max_length = max(max_length, curr_len)
        return max_length
