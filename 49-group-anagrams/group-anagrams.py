from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            counts[key].append(i)
        return list(counts.values())
