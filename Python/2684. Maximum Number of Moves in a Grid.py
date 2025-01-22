class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        
        # DP
        dp = []
        for i in range(row):
            dp.append([0]*col)

        # recur
        def move(row, col):
            # last col
            if col == col-1:
                return 0
            
            # cache
            if dp[row][col] != 0:
                return dp[row][col]

            ans = 0
            dir = [-1, 0, 1]

            for i in dir:
                newRow = row + i
                newCol = col + 1

                if 0 <= newRow < len(grid) and newCol < len(grid[0]) and grid[newRow][newCol] > grid[row][col]:
                    ans = max(ans, move(newRow, newCol) + 1)
            
            dp[row][col] = ans
            
            return ans

        # call recur
        ans = 0
        for i in range(row):
            ans =  max(ans, move(i, 0))
        
        return ans
        
s = Solution()
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
print(s.maxMoves(grid))