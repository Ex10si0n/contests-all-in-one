'''
Algorithms Tags: None
Efficiency: Normal
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = x
        rev = 0
        while a != 0:
            i = a % 10
            a //= 10
            rev = rev * 10 + i
        if rev == x:
            return True
        return False

