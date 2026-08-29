class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            x = target - n
            if x in d:
                return [d[x], i]
            else:
                d[n] = i
                