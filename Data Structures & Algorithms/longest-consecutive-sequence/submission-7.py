class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        cur_len = 1
        max_len = 1
        for i in range(len(nums) - 1):
                
            if nums[i+1] == nums[i] + 1:
                cur_len += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                cur_len = 1
                
            if cur_len > max_len:
                max_len = cur_len

        return max_len
            

        