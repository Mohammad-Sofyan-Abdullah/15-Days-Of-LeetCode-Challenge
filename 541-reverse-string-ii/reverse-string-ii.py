class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0,len(s),2*k):
            sub = s[i:i+k]
            print (sub)
            sub = sub[::-1]
            s = s[:i]+sub+s[i+k:]
        return s
#         s = list(s)
#         for i in range(0, len(s), 2*k):
#             s[i:i+k] = reversed(s[i:i+k])
        
#         # print(s)
#         s = "".join(s)
#         print(s)
#         return s
        
            