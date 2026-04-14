from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        result=[]
        for key,value in c.items():
            result.append([value,key])
        result.sort()
        arr=[]
        while len(arr)<k:
            arr.append(result.pop()[1])
        return arr

