import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=re.sub(r'[^a-zA-Z0-9]','',s)
        clean_s_lower=clean_s.lower()
        i=0;r=len(clean_s_lower)-1
        for i in range(len(clean_s_lower)):
            if clean_s_lower[i]==clean_s_lower[r]:
                i+=1
                r-=1
            else:
                return False
        return True