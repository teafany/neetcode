class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            w = r - l
            h = min(heights[r], heights[l])
            area = w * h
            max_water = max(area, max_water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water