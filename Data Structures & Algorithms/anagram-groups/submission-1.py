from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for word in strs:
            result=''.join(sorted(word))
            groups[result].append(word)
        return list(groups.values())