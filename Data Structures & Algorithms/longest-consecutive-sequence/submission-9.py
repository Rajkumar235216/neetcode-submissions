class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_consecutive = 0
        length = 0
        for n in nums:
            if n - 1 not in s:
                length = 1
                while length < len(nums):
                    if n+length in s:
                        length += 1
                    else:
                        break
            
            max_consecutive = max(max_consecutive, length)

        return max_consecutive
            
            
            

        