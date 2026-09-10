class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minV = nums[-1]
        
        while l <= r:
            if r > len(nums) - 1:
                break
            mid = (l + r)//2
            print("l -- ", l, "r -- ", r)
            print("mid -- ", mid)
            print("minV -- ", minV)
            print("nums[mid] -- ", nums[mid])
            if self.feasible(minV ,nums[mid]):
                l = mid + 1
                
            else:
                minV = nums[mid]
                r = mid - 1
        return minV


    def feasible(self, val1: int, val2: int):
        if val1 < val2:
            return True
        else:
            return False