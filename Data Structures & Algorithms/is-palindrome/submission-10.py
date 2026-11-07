class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
       
        while left < right:
            while left < right and not self.isAlpha(s[left].lower()):
                left += 1
                
            while right > left and not self.isAlpha(s[right].lower()):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left +=1
            right -=1 

        return True  


    def isAlpha(self, c):
        return ord('a') <= ord(c) <= ord('z') or \
            ord('0') <= ord(c) <= ord('9') 