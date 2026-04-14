from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        res=[]
        for i in nums:
            d[i]+=1
        for k in d.keys():
            if d[k]>len(nums)//3:
                res.append(k)
        return res