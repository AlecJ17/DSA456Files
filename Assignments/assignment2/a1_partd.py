# copy over your a1_partd.py file here
from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_list = []

    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1) and (c == 0 or c == cols - 1):
                neighbors = 2
            elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                neighbors = 3
            else:
                neighbors = 4


            if abs(grid[r][c]) >= neighbors:
                overflow_list.append((r, c))

    return overflow_list if overflow_list else None

def overflow(grid, a_queue):


    def spread_overflow(row, col, Sign):
        #get neighbors around row ,col
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]


        #loop all neighbors if row and col in len(grid)

        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] < 0:
                    grid[r][c] -= 1
                else:
                    grid[r][c] +=1
        # change Sign
        for r, c in neighbors:
            if Sign and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] >0:
                grid[r][c]*=-1
            if not Sign and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] <0:
                grid[r][c]*=-1

    steps = 0
    while True:
        overflow_list = get_overflow_list(grid)
        if not overflow_list:
            break

        for r, c in overflow_list:
            isNegative = (grid[r][c]<0)
            if (r, c-1) not in overflow_list and (r-1,c) not in overflow_list:
                grid[r][c] = 0
            if (r, c-1) in overflow_list:
                if (r-1,c)  in overflow_list:
                    grid[r][c] = 2
                grid[r][c] = 1

            spread_overflow(r, c, isNegative)

        a_queue.enqueue([row[:] for row in grid])
        steps += 1
        #Modified for partA
        negativeSign = True
        positiveSign = True
        for row in grid:
            for cell in row:
                if cell >= 0:
                    negativeSign = False
                if cell < 0:
                    positiveSign = False
        if negativeSign or positiveSign:
            a_queue.enqueue([row[:] for row in grid])
            return True
    return steps

