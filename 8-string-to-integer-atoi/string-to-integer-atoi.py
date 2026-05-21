class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        i=0

        s=s.lstrip()
        
        if not s:
            return 0

        if s[0]=="-":
            sign=-1
            i=1
            
        elif s[0]=="+":
            i=1
        

        def jihad(n,num):
            if n>=len(s) or not s[n].isdigit():
                return num
            
            num=num*10+int(s[n])

            return jihad(n+1,num)
           
            

        result=sign*jihad(i,0)

        mi=-2**31
        ma=2**31-1

        if result<mi:
            return mi
        
        if result>ma:
            return ma

        return result
        
        
            

