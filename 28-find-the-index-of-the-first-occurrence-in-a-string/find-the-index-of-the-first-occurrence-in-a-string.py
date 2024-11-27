class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Solution 1
#         if not needle:
#             return 0
    
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i

#         return -1

        #Solution 2 One Liner 
        return haystack.find(needle)
