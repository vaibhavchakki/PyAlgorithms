# https://leetcode.com/problems/similar-rgb-color/description/
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.

class Solution(object):
    def get_closest_num(self, num):

        nums = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
        index = int(num, 16) // 0x10
        min_array = [nums[index]]
        
        if index == 0:
            min_array.append(nums[index + 1])
        elif index == 0xf:
            min_array.append(nums[index - 1])
        else:
            min_array.append(nums[index + 1])
            min_array.append(nums[index - 1])

        return min(min_array, key = lambda x: abs(int(num, 16) - int(x, 16)))
            
        
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        strings = [self.get_closest_num(color[n:n+2]) for n in range(1, len(color), 2)]
        return "#" + "".join(strings)