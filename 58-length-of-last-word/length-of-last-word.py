class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        arr = s.split(" ")
        print(arr)
        arr = [i for i in arr if i != ""]
        print(arr)
        n = len(arr[-1])
        
        return n