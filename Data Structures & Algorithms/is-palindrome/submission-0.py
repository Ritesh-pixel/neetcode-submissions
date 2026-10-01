class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch.lower() for ch in s if ch.isalnum())
        if s[::1]==s[::-1]:
            return(True)
        else:
            return(False)