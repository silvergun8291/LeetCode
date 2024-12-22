class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ''.join(ch for ch in s.lower() if ch.isalnum())
        return sentence == sentence[::-1]