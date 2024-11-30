class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # arr = s.split(" ")
        # print(arr)
        # arr = [i for i in arr if i != ""]
        # print(arr)
        # n = len(arr[-1])
        
        arr = s.split()
        if not arr:
            return 0
        return len(arr[-1])
        
