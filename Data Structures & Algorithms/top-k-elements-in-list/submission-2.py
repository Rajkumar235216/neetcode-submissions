from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for char in c:
            heapq.heappush(h, [c[char], char])
            if len(h) > k:
                heapq.heappop(h)
        
        output = []
        for val in h:
            output.append(val[1])

        return output