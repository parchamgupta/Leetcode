class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        seen = set([tuple(entrance)])
        m, n = len(maze), len(maze[0])
        result = 0
        arr = [entrance]
        while arr:
	        temp = []
	        for i, j in arr:
		        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			        x, y = i + dx, j + dy
			        if 0 <= x < m and 0 <= y < n:
				        if maze[x][y] != "+" and (x, y) not in seen:
					        seen.add((x, y))
					        temp.append((x, y))
			        else:
			        	if (i, j) != tuple(entrance):
					        return result
	        if temp:
		        result += 1
	        else:
		        return -1
	        arr = temp