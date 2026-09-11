class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        result = -1

        while l <= r:
            print("l -- ", l)
            print("r -- ", r)
            # if nums[l] == target:
            #     result = l
            #     return result
            # if nums[r] == target:
            #     result = r
            #     return result
            mid = (l + r) // 2
            print("mid -- ", mid)
            print("nums[mid]", nums[mid])
            if nums[mid] == target:
                result = mid
                return result

            # left sorted array
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                

        return result