class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Solution 1
        # n = []
        # k = 0
        # for i in nums:
        #     if i in n:
        #         continue
        #     else:
        #         n.append(i)
        #         k = k+ 1
        # print(n)
        # print(len(n))
        # nums[:len(n)] = n
        # return len(n)
    
        s = set()
        k = 0
        for i in nums:
            if i not in s:
                s.add(i)
                nums[k] = i
                k += 1
        return k
                
            
        