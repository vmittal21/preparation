# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.
# https://leetcode.com/problems/trapping-rain-water/

# Brute force approach

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water = 0
        curr_loc = 0
        while curr_loc < len(height):
             maxL = max(height[:curr_loc+1])
             maxR = max(height[curr_loc:])
             curr_water = min(maxL, maxR) - height[curr_loc]
             total_water += curr_water
             curr_loc +=1
        return total_water