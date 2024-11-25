class Solution(object):
    def isPalindrome(self, s):
        # """
        # :type s: str
        # :rtype: bool
        # """

        # Solution 1

        s_new = ""
        # n = ' '
        # if n == ' ':
        #     print('true')

        for i in s:
            print(i)
            if i.isdigit() | i.isalpha():
                print(i)
                s_new = s_new + i
            elif i == ' ':
                continue
            else:
                continue

        s_new = s_new.lower()
        reverse_s_new = s_new[::-1]
        print(reverse_s_new)
        print(s_new)

        if s_new == reverse_s_new:
            return True
        else:
            return False

        #Solution 2

        # filtered = ''.join(char.lower() for char in s if char.isalnum())
    
        # return filtered == filtered[::-1]

        