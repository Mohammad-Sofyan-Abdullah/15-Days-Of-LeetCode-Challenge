class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = []
        k = 0
        for i in nums:
            if i in n:
                continue
            else:
                n.append(i)
                k = k+ 1
        print(n)
        print(len(n))
        nums[:len(n)] = n
        return len(n)
                
            
        