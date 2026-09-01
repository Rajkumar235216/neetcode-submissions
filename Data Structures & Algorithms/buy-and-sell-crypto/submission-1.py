class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = len(prices) - 1
        minPrice = 0
        maxPrice = 0
        while l <= r:
            if l == 0:
                minPrice = prices[l]
                l += 1
                continue
            print("l -- ", prices[l])
            print("minPrice --", minPrice)
            print("maxProfit -- ", maxProfit)
            maxProfit = max(prices[l] - minPrice, maxProfit)
            minPrice = min(minPrice, prices[l])
            l += 1
        return maxProfit