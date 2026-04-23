class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        a=x[::-1]
        if a[-1]=="-":
            a="-"+a[:-1]
        result=  int(a)

        if result < -2**31 or result > 2**31 -1:
            return 0
        
        return result