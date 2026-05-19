class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        left=0
        right=0
        x=[]
        m=0
        for i in s:
            if i not in a:
                a.add(i)
            
        while right<len(s):
            if s[right] not in x:
                x.append(s[right])
                m=max(m,len(x))
                right+=1
            else:
                x.remove(s[left])
                left+=1

        return m
        
        
        
        
        
        
        
        
        # Failed attempt:
        # # for j,y in enumerate(s):
        # for y in s:
        #     if y in b and y in a:
        #         b.clear()
        #         b.append(y)
        #         m=max(m,len(b))
            
        #     # elif y in a and y not in b:
        #     #     b.append(y)
        #     #     m=max(m,len(b))
        #     else:
        #         b.append(y)
        #         m=max(m,len(b))

        # return m



            