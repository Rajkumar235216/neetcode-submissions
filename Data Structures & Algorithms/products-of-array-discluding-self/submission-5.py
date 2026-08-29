class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = 1
        answer = [1]*length
        for i, n in enumerate(nums):
            if i == 0:
                answer[i] = 1
                left_product *= n
            else:
                answer[i] = left_product
                left_product *= n

        # print("left_product", left_product)
        # print("answer", answer)

        j = length - 1
        right_product = 1
        for n in nums[length-1: 0: -1]:
            # print('n', n)
            if j + 1 == length:
                answer[j] *= right_product
                right_product *= n
            else:
                answer[j] = answer[j] * right_product
                right_product *= n
            j -= 1
        answer[0] = right_product
        # print("right_product", right_product)
        return answer
