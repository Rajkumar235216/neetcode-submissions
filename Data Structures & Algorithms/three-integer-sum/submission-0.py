class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = list()
        d = {}
        length = len(nums)
        if length == 0:
            return []
        nums.sort()
        i = 0
        for i in range(length-1):
            # print("i", i)
            # print("nums", nums)
            first = nums[i]
            if first > 0:
                break
            j = i + 1
            k = length - 1
            while j < k:
                sum = first + nums[j] + nums[k]
                if sum == 0:
                    if f'{first},{nums[j]},{nums[k]}' not in d:
                        d[f'{first},{nums[j]},{nums[k]}'] = 1
                        triplets.append([first, nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            
        return triplets
                    