class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         solution = list()
        
#         for i in range(0, len(nums)):
#             j = i + 1
#             for j in range((i+1), len(nums)):
#                 k = j
#                 for j in range((j+1), len(nums)):
#                     if (i != j) & (i != k) & (j != k):
#                         if nums[i] + nums[j] + nums[k] == 0:
#                             solution.append(sorted([nums[i], nums[j], nums[k]]))
#                         else:
#                             continue
#                     else:
#                         continue
        

        

#         unique_list = [list(x) for x in set(tuple(x) for x in solution)]

#         print(unique_list)
        
        
#         return unique_list

        solution = list()
        zeroCounter = 0
        
        for num in nums:
            if num == 0:
                zeroCounter = zeroCounter + 1
            
        print(zeroCounter)
        if zeroCounter >= 3:
            solution.append([0, 0, 0])
            
        if 0 in nums:
            for num in nums:
                if num != 0:
                    if -1 * num in nums:
                        solution.append(sorted([-num, 0, num]))
                    
        n, p = [], []
        
        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
        
        P, N = set(p), set(n)
    
        for i in range(len(n)):
            for j in range(i + 1, len(n)): 
                x, y = n[i], n[j]
                target = -1 * (x + y)
                if target in P:
                    solution.append(tuple(sorted([x, y, target])))

        
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                x, y = p[i], p[j]
                target = -1 * (x + y)
                if target in N:
                    solution.append(tuple(sorted([x, y, target])))

        solution =  [list(x) for x in solution]
        
        unique_list = [list(x) for x in set(tuple(x) for x in solution)]

        print(unique_list)
        
        
        return unique_list


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        