class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        x=[]

        for i in s:
            if i!=" ":
                x.append(i)
            
            elif x:
                stack.append("".join(x))
                x=[]

        if x:
            stack.append("".join(x))
        
        result=[]
        while stack:
            result.append(stack.pop())

        return " ".join(result)

