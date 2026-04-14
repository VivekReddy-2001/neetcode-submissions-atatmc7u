class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''.join([char for char in s if char.isalnum()]).lower()
        s1=res[::-1]
        if s1==res:
            return True
        else:
            return False

        