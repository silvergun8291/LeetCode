class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch for ch in s.lower() if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z']
        return s == s[::-1]
        