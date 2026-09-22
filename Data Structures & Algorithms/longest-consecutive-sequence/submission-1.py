class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 1 # start of sequence
                while (n + 1) in nums_set:
                    length += 1
                    n += 1
                longest = max(longest, length)
        return longest