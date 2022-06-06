class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [x for x in s if x.isalpha() or x.isdigit()]
        s = ''.join(lst).lower()

        return s == s[::-1]