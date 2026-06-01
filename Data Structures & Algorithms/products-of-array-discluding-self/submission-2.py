class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        p_a = [1]*n
        for i in range(n):
            p_a[i] = prefix
            prefix *= nums[i]

        for i in range(n - 1, -1, -1):
            p_a[i] *= suffix
            suffix *= nums[i]
        

        return p_a
                