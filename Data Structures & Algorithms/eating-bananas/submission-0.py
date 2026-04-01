class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if not self.allBananasEaten(piles, h, mid):
                left = mid + 1
            else:
                right = mid - 1

        return left

    def allBananasEaten(self, piles, h, k):
        
        piles_list = piles
        for i in range(len(piles_list)):
            h -= math.ceil(piles_list[i] / k)
        
        if h < 0:
            return False
        else:
            return True

