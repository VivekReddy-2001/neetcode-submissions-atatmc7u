class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum=0
        for i in range(0, len(prices)):
            current_sum=0
            for j in range(i+1,len(prices)):
                current_sum=prices[j]-prices[i]
                max_sum=max(current_sum,max_sum)
        return max_sum
        