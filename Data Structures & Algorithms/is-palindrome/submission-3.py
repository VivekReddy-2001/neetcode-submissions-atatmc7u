import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. remove non-alphanumeric
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        # 2. lowercase
        clean_s = clean_s.lower()
        i, r = 0, len(clean_s) - 1

        while i < r:              
            if clean_s[i] != clean_s[r]:
                return False       
            i += 1                 
            r -= 1

        return True