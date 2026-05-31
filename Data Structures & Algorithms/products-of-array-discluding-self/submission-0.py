class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_a = []
        multiplier = 1
        i = 0
        j = 0
        while i < len(nums):
            if i == j:
                j += 1
            if j == len(nums):
                i += 1
                j = 0
                p_a.append(multiplier)
                multiplier = 1
                
            multiplier *= nums[j]
            j += 1

        return p_a
                