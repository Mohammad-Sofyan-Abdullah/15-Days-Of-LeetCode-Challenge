class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        for i in range(len(s)):
            lt=[]
            c=0
            j=i
            for j in range(i,len(s)):
                if s[j] not in lt:
                    lt.append(s[j])
                    c+=1
                    if c>max:
                        max=c
                else:
                    break
        return max
#         char_index = {}  # Dictionary to store the last seen index of characters
#         max_length = 0
#         left = 0  # Left pointer of the sliding window

#         for right in range(len(s)):
#             if s[right] in char_index and char_index[s[right]] >= left:
# # Move the left pointer to the right of the last occurrence of the character
#                 left = char_index[s[right]] + 1
# # Update the last seen index of the current character
#             char_index[s[right]] = right

#             # Calculate the maximum length of the substring
#             max_length = max(max_length, right - left + 1)

#         return max_length