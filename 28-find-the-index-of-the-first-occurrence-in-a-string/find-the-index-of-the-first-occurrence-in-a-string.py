class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left=0
        right=0

        # while right<len(haystack):
        #     if haystack[right]==needle[0]:
        #         left=right
        #         right+=1
            
        #     if haystack[right]==needle[-1]:
        #         return left-

        if needle=="":
            return 0

        left=0
        right=len(needle)

        while right<=len(haystack):
            if haystack[left:right]==needle:
                return left
            else:
                left+=1
                right+=1

        return -1
