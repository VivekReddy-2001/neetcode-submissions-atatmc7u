from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count=defaultdict(int)
        t_count=defaultdict(int)

        for i in s:
            s_count[i]+=1
        for i in t:
            t_count[i]+=1
        
        if s_count==t_count:
            return True
        return False