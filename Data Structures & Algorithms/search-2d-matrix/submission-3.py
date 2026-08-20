class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0]) #len of 0th row is no. of cols

        top, bot = 0, ROWS-1
        while top <= bot :
            row = (top+bot)//2

            if target > matrix[row][-1]: #last element of middle row
                top = row + 1
            elif target < matrix[row][0]: #first element of middle row
                bot = row - 1
            else :
                break #either we found our target within that row else not present anywhere
            
        if not (top <= bot):
             return False

        row = (top+bot)//2
        l, r = 0, COLS - 1 #Last valid index for r
        while l <= r :
            m = (l+r)//2
            if target > matrix[row][m] :
                l = m+1
            elif target < matrix[row][m] :
                r = m-1
            else :
                return True
        return False
        
        