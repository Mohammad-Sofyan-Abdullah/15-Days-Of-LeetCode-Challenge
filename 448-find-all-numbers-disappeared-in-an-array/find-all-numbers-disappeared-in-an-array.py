class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #Solution 1 Brute Force
#         length = len(nums)
#         nums = set(nums)
#         new_nums = []
#         for i in range(1, length+1):
#             if (i not in nums):
#                 new_nums.append(i)
            
            
                

#         return new_nums
        
        #Solution 2 Onliner brute force\U0001f602\U0001f602\U0001f602\U0001f602
        return list(set(range(1, len(nums)+1)) - set(nums))
