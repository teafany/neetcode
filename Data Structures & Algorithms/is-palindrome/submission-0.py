class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(strip) - 1
        while l < r:
            if strip[l] != strip[r]:
                return False
            l += 1
            r -= 1
        return True
