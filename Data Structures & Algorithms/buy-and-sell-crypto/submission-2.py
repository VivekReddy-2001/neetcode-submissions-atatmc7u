class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum=0
        l,r=0,1

        while r<len(prices):
            if prices[r]>prices[l]:
                max_sum=max((prices[r]-prices[l]),max_sum)
                r+=1
            else:
                l=r
                r+=1
        return max_sum
        