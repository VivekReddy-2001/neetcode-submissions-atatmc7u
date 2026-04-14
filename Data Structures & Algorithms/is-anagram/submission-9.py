
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        for i in s:
            s1[i] = s1.get(i, 0) + 1
        s2={}
        for i in t:
            s2[i] = s2.get(i, 0) + 1
        return s1 == s2