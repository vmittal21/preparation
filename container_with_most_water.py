# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.

# https://leetcode.com/problems/container-with-most-water/

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Solution:


from collections import defaultdict
class Solution:
         
    # Shrinking the window approach is used traversing from left and right towards the middle
     
    def maxArea(self, height: List[int]) -> int:
              
        ptr1 = 0
        ptr2 = len(height)-1
        max_area = 0
        
        while ptr1 < ptr2:
           area = min(height[ptr1],height[ptr2]) * (ptr2-ptr1)
           max_area = max(max_area, area)
                
           if height[ptr1] <= height[ptr2]:
                ptr1+=1
           else:
                ptr2-=1 
                
        return max_area
        