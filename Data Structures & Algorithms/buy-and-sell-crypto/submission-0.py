class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        p = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                pr = prices[r] - prices[l]
                p = max(p, pr)
            else:
                l = r
            r += 1
        return p