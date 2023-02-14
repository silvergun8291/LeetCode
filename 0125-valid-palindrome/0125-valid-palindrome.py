class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        # Remove special characters, convert to lowercase
        for ch in s:
            if ch.isalnum():
                strs.append(ch.lower())

        if strs == list(reversed(strs)):
            return True
        else:
            return False