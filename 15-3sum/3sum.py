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

    #Solution 2
#         solution = list()
#         zeroCounter = 0
        
#         for num in nums:
#             if num == 0:
#                 zeroCounter = zeroCounter + 1
            
#         print(zeroCounter)
#         if zeroCounter >= 3:
#             solution.append([0, 0, 0])
            
#         if 0 in nums:
#             for num in nums:
#                 if num != 0:
#                     if -1 * num in nums:
#                         solution.append(sorted([-num, 0, num]))
                    
#         n, p = [], []
        
#         for i in nums:
#             if i > 0:
#                 p.append(i)
#             elif i < 0:
#                 n.append(i)
        
#         P, N = set(p), set(n)
    
#         for i in range(len(n)):
#             for j in range(i + 1, len(n)): 
#                 x, y = n[i], n[j]
#                 target = -1 * (x + y)
#                 if target in P:
#                     solution.append(tuple(sorted([x, y, target])))

        
#         for i in range(len(p)):
#             for j in range(i + 1, len(p)):
#                 x, y = p[i], p[j]
#                 target = -1 * (x + y)
#                 if target in N:
#                     solution.append(tuple(sorted([x, y, target])))

#         solution =  [list(x) for x in solution]
        
#         unique_list = [list(x) for x in set(tuple(x) for x in solution)]

#         print(unique_list)
        
        
#         return unique_list

        if len(nums) < 3:
            return []

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

            # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
            if len(z) >= 3:
                res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        from itertools import combinations

        for x, y in combinations(n, 2):
            target = -1 * (x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set

        for x, y in combinations(p, 2):
            target = -1 * (x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        