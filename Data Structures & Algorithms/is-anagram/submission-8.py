from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # countS=defaultdict(int)
        # countT=defaultdict(int)

        # for i in range(len(s)):
        #     countS[s[i]]+=1
        #     countT[t[i]]+=1
        
        # if countS!=countT:
        #     return False
        # return True
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        for val in count:
            if val!=0:
                return False
        return True