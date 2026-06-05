class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        # if numbers[mid] >= target:
        #     end = mid - 1
        # else:
        #     start = mid += 1
        
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]

            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

            # if abs(numbers[start]) >= target:
            #     start += 1
            # elif abs(numbers[end]) >= target:
            #     end -= 1
            # else:
            #     start += 1
            # if (numbers[start]) >= target:
            #     start += 1
            # elif (numbers[end]) >= target:
            #     end -= 1
            # else:
            #     start += 1
                
            