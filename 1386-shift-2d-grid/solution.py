class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col_len , row_len = len(grid) , len(grid[0])

        tem_grid = []

        # convert to flat list
        for row in grid:
            tem_grid.extend(row)

        # shift k times
        k %= (col_len * row_len)
        tem_grid = tem_grid[-k:] + tem_grid[:-k]

        # again convert to 2D
        final_grid = []
        idx = 0

        for z in range(col_len):
            final_grid.append(tem_grid[idx : idx + row_len])
            idx += row_len

        return final_grid


            
