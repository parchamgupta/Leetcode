class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        c = len(grid[0])
        up = 1
        left = 2
        right = 3
        
        def func(y):
            f = up
            x = 0
            while x < r:
                if not (0 <= y < c):
                    return -1
                if grid[x][y] == 1:
                    if f == up:
                        f = left
                        y += 1
                    elif f == left:
                        f = up
                        x += 1
                    else:
                        return -1
                else:
                    if f == up:
                        f = right
                        y -= 1
                    elif f == left:
                        return -1
                    else:
                        f = up
                        x += 1
            return y
            
        ans = []
        for y in range(c):
            ans.append(func(y))
        return ans