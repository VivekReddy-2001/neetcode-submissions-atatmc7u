class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best=0
        freq={}
        l=0

        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            while (r-l+1)- max(freq.values()) >k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            best=max(best,r-l+1)
        return best