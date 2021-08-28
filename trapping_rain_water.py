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

# optimization using 2 pointers approach:

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water = 0
        right_ptr = len(height)-1
        left_ptr = 0
        maxL = 0
        maxR=height[right_ptr]
        
        while left_ptr < right_ptr:
                                       
             if height[left_ptr]<=height[right_ptr]:
                if height[left_ptr]>=maxL:
                    maxL = height[left_ptr] 
                else:
                    total_water += maxL-height[left_ptr]
                left_ptr+=1
                
             else:
                 if height[right_ptr]>=maxR:
                     maxR = height[right_ptr]   
                 else:
                     total_water += maxR-height[right_ptr]
                 right_ptr-=1
                
        return total_water  

