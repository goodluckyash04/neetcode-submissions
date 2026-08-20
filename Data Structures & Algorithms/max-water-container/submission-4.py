class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_w = 0
        while l < r:
            height = min(heights[l], heights[r]) 
            width = r - l
            area = height * width
            max_w = max(area, max_w)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_w

        
            
