class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = -1

        l,r = 0,m-1
        while l<=r:
            mid = l + (r-l)//2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                row = mid
                break
            elif target > matrix[mid][n-1]:
                l = mid+1
            else:
                r = mid-1
        if row == -1:
            return False

        l,r = 0, n-1
        while l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l = mid+1
        return False    