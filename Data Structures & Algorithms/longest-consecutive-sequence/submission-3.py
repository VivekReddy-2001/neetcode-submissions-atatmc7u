class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums=set(nums)
        res=0
        for num in s_nums:
            curr=num
            streak=0
            while curr in s_nums:
                streak+=1
                curr+=1 
            res=max(res,streak)
        return res
