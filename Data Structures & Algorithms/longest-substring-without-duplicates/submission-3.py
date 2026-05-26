class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    max_length=max(max_length,len(seen))
                else:
                    break
        return max_length
            