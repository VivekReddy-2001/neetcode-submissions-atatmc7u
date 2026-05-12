from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=Counter(nums)
        s1=dict(sorted(s.items(),key=lambda item:item[1],reverse=True))
        l=[]
        c=0
        for key,v in s1.items():
            if c==k:
                return l
            l.append(key)
            c+=1 
        return l