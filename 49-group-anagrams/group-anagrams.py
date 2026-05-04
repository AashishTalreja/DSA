class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x={}
        for i in range(len(strs)):
            y=tuple(sorted([ord(a) for a in strs[i]]))
            if y not in x:
                x[y]=[]
            x[y].append(strs[i])
        return list(x.values())


