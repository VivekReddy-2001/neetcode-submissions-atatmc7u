class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2=list(set(nums))
        if len(nums)==len(nums2):
            return False
        return True



            
         