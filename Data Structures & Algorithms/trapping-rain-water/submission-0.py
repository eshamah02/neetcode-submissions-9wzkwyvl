class Solution:
    # calculate trapped water at some index i where l is the greatest 
    # value to the left and r is the greatest value to the right
    def calc_trap(self, height: List[int], l_val: int, r_val: int, i: int) -> int:
        trap = max(0, min(l_val, r_val) - height[i])
        return trap

    def greatest_left_vals(self, height: List[int]) -> dict:
        greatest_left = {}
        l_max = 0

        for i in range(len(height)):
            greatest_left[i] = l_max
            l_max = max(l_max, height[i])
            
        return greatest_left

    def greatest_right_vals(self, height: List[int]) -> dict:
        greatest_right = {}
        r_max = 0

        for i in range(len(height) - 1, -1, -1):
            greatest_right[i] = r_max
            r_max = max(r_max, height[i])
            
        return greatest_right


    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 1:
            return 0

        greatest_left = self.greatest_left_vals(height)
        greatest_right = self.greatest_right_vals(height)

        total_trap = 0

        for i in range(len(height)):
            trapped_i = self.calc_trap(height, greatest_left[i], greatest_right[i], i)
            total_trap += trapped_i

        return total_trap



        