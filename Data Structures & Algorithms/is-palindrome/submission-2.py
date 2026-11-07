class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right > -1 :
                right -= 1

            # print(s[left], s[right])
            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

            
        return True