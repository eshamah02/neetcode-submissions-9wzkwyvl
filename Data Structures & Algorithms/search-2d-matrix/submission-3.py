class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) - 1
        target_row = -1

        for row in range(len(matrix)):
            if target >= matrix[row][0] and target <= matrix[row][m]:
                target_row = row

        if target_row < 0:
            return False

        target_arr = matrix[target_row]

        left = 0
        right = m

        while left <= right:
            mid = (left + right) // 2
            if target < target_arr[mid]:
                right = mid - 1
            elif target > target_arr[mid]:
                left = mid + 1
            else:
                return True

        return False
