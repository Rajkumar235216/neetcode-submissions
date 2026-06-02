class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        last = nums[0]
        j = 0
        cd = {0: [last]}
        mx_array = [0]
        for i in range(len(nums) - 1):
            if nums[i+1] == last + 1:
                last += 1
                cd[j].append(last)
                mx_array[j] = len(cd[j])
            elif nums[i+1] == last:
                mx_array[j] = len(cd[j])
                continue
            else:
                print("here")
                last = nums[i+1]
                j = j + 1
                cd[j] = [last]
                mx_array.append(len(cd[j]))
       
        return max(mx_array)
            

        