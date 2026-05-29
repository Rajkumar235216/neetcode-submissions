class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}

        for num in nums:
            if num not in elements:
                elements[num] = 0
            else:
                elements[num] += 1

        if len(elements) == 1:
            return list(elements.keys())

        sorted_dict = sorted(elements.items(), key=lambda item: item[1], reverse=True)
        i = 0
        frequent_elem_list = []
        print(sorted_dict)
        for key, val in sorted_dict:
            if i < k:
                frequent_elem_list.append(key)
                i += 1
            else:
                return frequent_elem_list
        return frequent_elem_list
