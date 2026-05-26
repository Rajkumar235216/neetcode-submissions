class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        length = len(nums)
        while i < len(nums):
            if j < length:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            else:
                i += 1
                j = i + 1
        return []
        