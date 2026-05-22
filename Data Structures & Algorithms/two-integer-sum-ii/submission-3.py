class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0;right=len(numbers)-1
        while left<right:
            sum_integers= numbers[left]+numbers[right]
            if sum_integers==target and left<right:
                return [left+1,right+1]
            elif sum_integers<target:
                left+=1
            else:
                right-=1
        return []