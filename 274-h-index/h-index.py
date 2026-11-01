class Solution:
    def hIndex(self, citations: list[int]) -> int:
        x=citations
        x.sort(reverse=True)
        
        count=0

        for i in range(len(x)):
            if x[i]>=i+1:
                count+=1
            else:
                break
        return count