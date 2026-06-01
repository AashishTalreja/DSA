class Solution:
    def reverseWords(self, s: str) -> str:
        # x=[]
        # left=0
        # right=len(s)-1
        

        # while left<right:
        #     if s[left]==" ":
        #         y="".join(s[:left])
        #         x.append(y)

        # return str(x)
                
        x=s.split()
        x=list(x)
        x.reverse()
        y=[]
        

        y=" ".join(x)

        return y
