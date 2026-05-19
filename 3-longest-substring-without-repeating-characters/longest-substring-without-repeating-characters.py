class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        z=set()
        l=0

        for r in range(len(s)):
            
            while s[r] in z:
                z.remove(s[l])
                l+=1
            
            z.add(s[r])
            ans=max(ans,r-l+1)

        return ans



        
        
        
        
        
        
        
        
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



            