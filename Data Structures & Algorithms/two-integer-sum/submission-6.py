class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for key,value in enumerate(nums):
            x=target-value
            if x in seen:
                return [seen[x],key]
            seen[value]=key