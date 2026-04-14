from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_element=len(nums)//2
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for i in d.keys():
            if d[i]>major_element:
                return i