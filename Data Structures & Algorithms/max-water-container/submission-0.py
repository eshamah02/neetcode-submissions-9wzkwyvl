class Solution:
    def calc_area(self, heights: List[int], l: int, r: int) -> int:
        area = min(heights[l], heights[r]) * (r - l)
        return area 

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        # how to calculate area between l and r? 
        # take min of l, r, multiply by difference between l and r
        max_area = self.calc_area(heights, l, r)
        print(f"max_area:{max_area}")

        while l < r:
            area = self.calc_area(heights, l, r)
            if area >= max_area:
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            


        return max_area




        