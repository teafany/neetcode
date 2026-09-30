class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        longest = 0
        l = 0

        for r in range(len(s)): # move r when valid window
            while s[r] in my_set:
                my_set.remove(s[l]) # invalid window
                l += 1 # move l when invalid window
            my_set.add(s[r])
            window = (r - l) + 1
            longest = max(longest, window)
        return longest